# import ocean_model_skill_assessor.plot as plot
import cook_inlet_catalogs as cic
import intake
import matplotlib.pyplot as plt
from ocean_model_skill_assessor.plot import line
import os
import pandas as pd
from pathlib import Path
import xarray as xr
import cf_pandas as cfp
import numpy as np

vocab=cic.utils.vocab
# import pdb; pdb.set_trace()
# vocab.vocab["east_rotate"] = {'name': '(?i)^east_rotate($|.+)'}
cfp.set_options(custom_criteria=vocab.vocab)

slugs = [        
    "adcp_moored_noaa_coi_other",
    "adcp_moored_noaa_coi_2005",
]
# model_names = ["ciofs_hindcast"]
model_names = ["ciofs_hindcast", "ciofs_fresh"]
key_variables=["east","north","speed"]  # the variables to include in the subplots. Should be 3
vardescs = ["Along-Channel Velocity [m/s]", "Cross-Channel Velocity [m/s]", "Speed [m/s]"]
# key_variables=["speed","along","across"]
# vardescs = ["Horizontal Speed", "Along-Channel Velocity", "Across-Channel Velocity"]

which = "_rotate"  # or "" for tidal
whichtitle = ""  # or "" for tidal
# which = "_rotate_subtidal"  # or "" for tidal
# whichtitle = "Subtidal"  # or "" for tidal

for slug in slugs:
    print(slug)
    loc = f"~/projects/cook-inlet-catalogs/cook_inlet_catalogs/catalogs/{slug}.yaml"
    cat = intake.open_catalog(loc)
    
    for dataset in list(cat):
        print(dataset)
        # obs = None
        obs = {key_variable: None for key_variable in key_variables}
        # models = []
        models = {key_variable: [] for key_variable in key_variables}
        for key_variable, vardesc in zip(key_variables, vardescs):
            
            for model in model_names:
                # print(model)
                path = Path(f"/home/kristen/.cache/ocean-model-skill-assessor/{slug}_{model}/processed/{slug}_{dataset}_{key_variable}{which}_model.nc")

                try:
                    models[key_variable].append(xr.open_dataset(path))
                except FileNotFoundError:
                    print(f"{path} not present, skipping dataset")
                    continue
                
                # ALSO SUBTIDAL
                
                if obs[key_variable] is None:
                    # print("obs None")
                    path = str(path).replace("_model.nc", "_data.nc")
                    obs[key_variable] = xr.open_dataset(path)


        # Plotting the ADCP time series
        # import pdb; pdb.set_trace()
        if len(models[key_variables[0]]) == 1 or len(models[key_variables[1]]) == 1:
            print(f"Only one model for {slug} {dataset}, skipping")
            continue

        # by depth UPDATE THIS
        # import pdb; pdb.set_trace() 
        if obs[key_variables[0]] is None:
            print(f"No observations for {slug} {dataset}, skipping")
            continue 
        
        depths = np.unique(obs[key_variables[0]].cf["depth"])


        for depth in depths:
            figname=f"figures/{slug}/{dataset}{which}/{str(abs(depth)).replace('.','_')}.png"
            print(figname)
            if Path(figname).exists():
                continue
            # import pdb; pdb.set_trace()
            figs, axes = [], []
            for key_variable, vardesc in zip(key_variables, vardescs):
                # obs[key_variable].where(obs[key_variable].cf["depth"] == depth, drop=True)
                # istation = obs[key_variable][obs[key_variable].cf["depth"] == depth].index.values
                # models_use = [m[istation] for m in models]
                # import pdb; pdb.set_trace()  
                models_use = [m.cf[key_variable].where(abs(m.cf[key_variable].cf["depth"]) == abs(depth), drop=True).to_dataset() for m in models[key_variable]]
                # models_use = [m.cf[key_variable][istation].to_dataset() for m in models[key_variable]]
            
                fig, ax = line.plot(
                    obs=obs[key_variable].where(abs(obs[key_variable].cf["depth"]) == abs(depth), drop=True).to_dataframe(),
                    model=models_use,
                    xname="T",
                    yname=key_variable,
                    # title=f"{slug} {dataset} {station} {vardesc}",
                    xlabel="",
                    ylabel=vardesc,
                    model_label=model_names,
                    # figname=f"figures/{slug}_{dataset}_{station}_{key_variable}.png",
                    dpi=100,
                    figsize=(15, 5),
                    return_plot=False,
                    return_fig_and_ax=True,
                )
                figs.append(fig)
                axes.append(ax)
        
            ax1, ax2, ax3 = axes[0], axes[1], axes[2]

            # make new plot from the two figs of the two variables
            fig_combined, (ax1_new, ax2_new, ax3_new) = plt.subplots(3, 1, figsize=(15, 10), sharex=True)

            # Copy lines from ax1 to ax1_new
            for l in ax1.get_lines():
                ax1_new.plot(*l.get_data(), label=l.get_label(), color=l.get_color(), ls=l.get_linestyle())

            # Copy lines from ax2 to ax2_new
            for l in ax2.get_lines():
                ax2_new.plot(*l.get_data(), label=l.get_label(), color=l.get_color(), ls=l.get_linestyle())

            # Copy lines from ax3 to ax3_new
            for l in ax3.get_lines():
                ax3_new.plot(*l.get_data(), label=l.get_label(), color=l.get_color(), ls=l.get_linestyle())

            # import pdb; pdb.set_trace()
            # ax1_new.set_title(ax1.get_title())
            # ax2_new.set_title(ax2.get_title())
            title=f"{slug}: {whichtitle} dataset: {dataset}, depth: {depth}"
            fig_combined.suptitle(title, fontsize=14)

            ax1_new.set_ylabel(ax1.get_ylabel())
            ax2_new.set_ylabel(ax2.get_ylabel())
            ax3_new.set_ylabel(ax3.get_ylabel())
            ax3_new.set_xlabel(ax3.get_xlabel())
            # ax2_new.set_ylabel(ax2.get_ylabel())
            
            ax1_new.set_xticklabels([])
            ax2_new.set_xticklabels([])
            ax3_new.set_xticklabels(ax3.get_xticklabels())

            # ax1_new.legend()
            # ax2_new.legend()
            ax3_new.legend()

            fig_combined.tight_layout()
            
            ax1_new.axis('tight') 
            ax2_new.axis('tight') 
            ax3_new.axis('tight') 

            os.makedirs(f"figures/{slug}/{dataset}{which}", exist_ok=True)
            fig_combined.savefig(figname, bbox_inches="tight", dpi=100)

            plt.close(figs[0])
            plt.close(figs[1])
            plt.close(figs[2])
            plt.close(fig_combined)

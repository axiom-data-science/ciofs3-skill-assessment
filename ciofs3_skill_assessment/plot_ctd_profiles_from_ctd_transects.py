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

vocab=cic.utils.vocab
cfp.set_options(custom_criteria=vocab.vocab)

slugs = [        
        #  "ctd_transects_barabara_to_bluff_2002_2003",
        # "ctd_transects_otf_kbnerr",  
        # "ctd_transects_cmi_kbnerr",  #
        # "ctd_transects_cmi_uaf", 
        "ctd_transects_gwa", #
        "ctd_transects_uaf",  #
]
model_names = ["ciofs_hindcast", "ciofs_fresh"]
key_variables=["temp","salt"]
vardescs = ["Sea temperature [C]", "Salinity"]
# featuretype = "profile"


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
                path = Path(f"/home/kristen/.cache/ocean-model-skill-assessor/{slug}_{model}/processed/{slug}_{dataset}_{key_variable}_model.nc")

                try:
                    models[key_variable].append(xr.open_dataset(path))
                except FileNotFoundError:
                    print(f"{path} not present, skipping dataset")
                    continue
                
                if obs[key_variable] is None:
                    # print("obs None")
                    path = str(path).replace("_model.nc", "_data.csv")
                    obs[key_variable] = pd.read_csv(path)
                

        # Plotting the CTD profiles
        if len(models[key_variables[0]]) == 1 or len(models[key_variables[1]]) == 1:
            continue

        # by station
        stations = obs[key_variables[0]].cf["station"].unique()


        for station in stations:
            figname=f"figures/{slug}/{dataset}/{str(station).replace('.','_')}.png"
            if Path(figname).exists():
                continue
            # import pdb; pdb.set_trace()
            figs, axes = [], []
            for key_variable, vardesc in zip(key_variables, vardescs):
                istation = obs[key_variable][obs[key_variable].cf["station"] == station].index.values
                # models_use = [m[istation] for m in models]
                models_use = [m.cf[key_variable][istation].to_dataset() for m in models[key_variable]]
                # import pdb; pdb.set_trace()
            
                fig, ax = line.plot(
                    obs=obs[key_variable].iloc[istation],
                    model=models_use,
                    xname=key_variable,
                    yname="Z",
                    # title=f"{slug} {dataset} {station} {vardesc}",
                    xlabel=vardesc,
                    ylabel="Depth [m]",
                    model_label=model_names,
                    # figname=f"figures/{slug}_{dataset}_{station}_{key_variable}.png",
                    dpi=100,
                    figsize=(4, 8),
                    return_plot=False,
                    return_fig_and_ax=True,
                )
                figs.append(fig)
                axes.append(ax)
        
            ax1, ax2 = axes[0], axes[1]

            # make new plot from the two figs of the two variables
            fig_combined, (ax1_new, ax2_new) = plt.subplots(1, 2, figsize=(7, 8))
            
            # Copy lines from ax1 to ax1_new
            for l in ax1.get_lines():
                ax1_new.plot(*l.get_data(), label=l.get_label(), color=l.get_color(), ls=l.get_linestyle())

            # Copy lines from ax2 to ax2_new
            for l in ax2.get_lines():
                ax2_new.plot(*l.get_data(), label=l.get_label(), color=l.get_color(), ls=l.get_linestyle())
            # import pdb; pdb.set_trace()
            # ax1_new.set_title(ax1.get_title())
            # ax2_new.set_title(ax2.get_title())
            title=f"{slug}: dataset: {dataset}, station: {station}"
            fig_combined.suptitle(title, fontsize=14)

            ax1_new.set_xlabel(ax1.get_xlabel())
            ax2_new.set_xlabel(ax2.get_xlabel())
            ax1_new.set_ylabel(ax1.get_ylabel())
            # ax2_new.set_ylabel(ax2.get_ylabel())

            ax1_new.legend()
            ax2_new.legend()
            
            fig_combined.tight_layout()

            os.makedirs(f"figures/{slug}/{dataset}", exist_ok=True)
            fig_combined.savefig(figname, bbox_inches="tight", dpi=100)

            plt.close(figs[0])
            plt.close(figs[1])
            plt.close(fig_combined)

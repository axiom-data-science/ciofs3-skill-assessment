import ocean_model_skill_assessor as omsa
# import ciofs_hindcast_report as chr
import intake
import cf_xarray as cfx
import cf_pandas as cfp

# import model_catalogs as mc
import xarray as xr
import pandas as pd

import extract_model as em
# import xroms
# import oceans.filters
import cmocean.cm as cmo
import cook_inlet_catalogs as cic


# model_slug = "v4j"
# cat_model = intake.open_catalog(f"models_{model_slug}.yaml")

cat_model = intake.open_catalog("models.yaml")


slugs = [        
        #  "ctd_transects_barabara_to_bluff_2002_2003",
        # "ctd_transects_otf_kbnerr",  
        # "ctd_transects_cmi_kbnerr",  #
        # "ctd_transects_cmi_uaf", 
        "ctd_transects_gwa", #
        # "ctd_transects_uaf",  #
        # 'ctd_transects_misc_2002',
]
models = ["ciofs3"]
# models = ["ciofs_hindcast"]
# models = ["ciofs_fresh", "ciofs_hindcast"]
key_variables=["temp","salt"]
vardescs = ["Sea temperature [C]", "Salinity"]

override_chunks = {"s_rho": 30, "s_w": 31}

for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    cat.metadata["name"] = slug
    for model in models:

        kwargs_plot = dict(
            # figsize=(20,6),
            # yincrease=False,
            # invert_yaxis=True,
            model_title=model.upper(),
            make_Z_negative = "obs",
        )
        project_name = f"{slug}_{model}"

        for key_variable, vardesc in zip(key_variables, vardescs):
            # add to kwargs_plot
            if key_variable == "temp":
                kwargs_plot["vmin_diff"] = -3
                kwargs_plot["vmax_diff"] = 3
            elif key_variable == "salt":
                kwargs_plot["vmin_diff"] = -2
                kwargs_plot["vmax_diff"] = 2
            slugdesc = (" ".join(slug.split("ctd_transects_")[1].split("_"))).title()
            plot_description = f"{slugdesc}: {vardesc} from CTD transect"
            omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                     preprocess=True,
                     vocabs="general", 
                     mode="a",
                     key_variable=key_variable, 
                     alpha=5, dd=5, 
                     interpolate_horizontal=True,
                     want_vertical_interp=True,
                     extrap=False,
                     model_source_name=model,
                     catalog_source_names=list(cat),
                     model_only=False,
                     # user_min_time=start_time_use, user_max_time=end_time_use,
                     check_in_boundary=False,
                     need_xgcm_grid=True,
                     # ts_mods=ts_mods,
                     plot_map=False,
                     vocab_labels="vocab_labels",
                     plot_count_title=False,
                         override_processed=False,
                         override_stats=False,
                         override_plot=False,
                         plot_description=plot_description,
                         kwargs_plot=kwargs_plot,

                    override_chunks=override_chunks,

                    )

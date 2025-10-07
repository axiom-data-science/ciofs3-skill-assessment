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


cat_model = intake.open_catalog("models.yaml")


slugs = [
  "ctd_profiles_ecofoci",
  "ctd_profiles_2005_noaa",
    "ctd_profiles_kachemack_kuletz_2005_2007",
    "ctd_profiles_kb_small_mesh_2006",
 'ctd_profiles_emap_2002',
 'ctd_profiles_emap_2008',
 'ctd_profiles_kbay_osu_2007',
 'ctd_profiles_piatt_speckman_1999',
 'ctd_profiles_usgs_boem',
]
# models = ["ciofs_fresh"]#,"ciofs_hindcast","ciofs3"]
# models = ["ciofs_hindcast"]
models = ["ciofs3"]
key_variables=["temp","salt"]
vardescs = ["Sea temperature [C]", "Salinity"]
wetdry=False

override_chunks = {"s_rho": 30, "s_w": 31}


for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    cat.metadata["name"] = slug

    for model in models:
        project_name = f"{slug}_{model}"
        kwargs_plot = {"model_label": model.upper()}

        for key_variable, vardesc in zip(key_variables, vardescs):
            plot_description = f"{vardesc} from CTD profile"
            omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                     preprocess=True,
                     vocabs=cic.utils.vocab,
                     # vocabs=["general", chr.vocab], 
                     mode="a",
                     key_variable=key_variable, 
                     alpha=5, dd=5, 
                     interpolate_horizontal=False,
                     want_vertical_interp=True,
                     model_source_name=model,
                     catalog_source_names=list(cat),
                     model_only=False,
                     # user_min_time=start_time_use, user_max_time=end_time_use,
                     check_in_boundary=True,  # some CTD profiles are outside the domain
                     need_xgcm_grid=True,
                     # ts_mods=ts_mods,
                     plot_map=False,
                     plot_count_title=False,
                     vocab_labels="vocab_labels",
                     plot_description=plot_description,
                     kwargs_plot=kwargs_plot,
                         override_model=False,
                         override_processed=False,
                         override_stats=False,
                         override_plot=False,
                    wetdry=wetdry,
                         
                    override_chunks=override_chunks,
                    )

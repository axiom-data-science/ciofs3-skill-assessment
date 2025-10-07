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
import oceans.filters
import cmocean.cm as cmo
import cook_inlet_catalogs as cic


cat_model = intake.open_catalog("models.yaml")


slugs = [        
        # "moorings_aoos_cdip",
        # "moorings_circac", 
        # "moorings_kbnerr", 
        # "moorings_kbnerr_bear_cove_seldovia", 
        # "moorings_kbnerr_historical",  # skipping for "1999-1-1","2002-1-1"
        # "moorings_kbnerr_homer",
        "moorings_noaa",    
        "moorings_nps",
        "moorings_uaf",  
         ]


# note that I ended up copying cached files for "ciofs_hindcast" from
# previous project instead of running this script


# models = ["ciofs3"]
# models = ["ciofs_hindcast", "ciofs_fresh"]
models = ["ciofs_hindcast"]


# for depth index need these to have model depths to choose index
# need_xgcm_grid=True,
# kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True),

# if slug in [        
#         "moorings_kbnerr_bear_cove_seldovia", 
#         "moorings_kbnerr_historical",  # 
#         "moorings_kbnerr_homer",
#          ]:
#     # for moorings that are below surface:
#     want_vertical_interp=False,
#     need_xgcm_grid=True,
#     kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True),
#     # override chunks -1 in vertical
#     # can I list these separately to run script
#     # also want_locstreamZ=True
#     want_locstreamZ=False

# override_chunks = {"s_rho": 30, "s_w": 31}

# for newer use ssh as mean, but then find index so no interp:
# need z_rho available to select nearest from
# no override chunks
# need_xgcm_grid=True,
# kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True),

wetdry = True

# if model == "ciofs_hindcast":
#     wetdry = True
# # elif model == "nwgoa":
# #     wetdry = False

key_variables = ["ssh"]
# key_variables = ["salt","ssh"]
# key_variables = ["temp","salt","ssh"]
# key_variables = ["temp"]
# key_variables = ["temp","salt"]

# time series for modification
def subtract_mean(dd, varname):
    if isinstance(dd, xr.DataArray):
        dd = dd.to_dataset()
    name = dd.cf[varname].name
    dd[name] = dd.cf[varname] - dd.cf[varname].mean()
    dd[name].name = name
    return dd

# apply subtidal filter across dataset
def subtidal_dataset(dd, varname):
    import cf_xarray
    # import pdb; pdb.set_trace()
    if isinstance(dd, xr.DataArray):
        dd = dd.to_dataset()
    dd[dd.cf[varname].name] = oceans.filters.pl33tn(dd.cf[varname], mode="same")
    return dd


for slug in slugs:

    # include non-surface stations
    if slug in [        
            "moorings_kbnerr_bear_cove_seldovia", 
            "moorings_kbnerr_historical",  # 
            "moorings_kbnerr_homer",
            ]:
        # for moorings that are below surface:
        want_vertical_interp=False,
        need_xgcm_grid=True,
        kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True),
        # override chunks -1 in vertical
        # can I list these separately to run script
        # also want_locstreamZ=True
        # want_locstreamZ=False
        want_locstreamZ=True
    else:
        want_vertical_interp=False,
        need_xgcm_grid=False,
        want_locstreamZ=False
        kwargs_xroms=dict()



    cat = intake.open_catalog(cic.utils.cat_path(slug))
    cat.metadata["name"] = slug

    source_names = list(cat)
    # source_names = ["noaa_nos_co_ops_9455595"]
    for source_name in source_names:

        for model in models:

            if model == "ciofs_hindcast":
                time_range = ["1999-1-1","2023-1-1"] 
            elif model == "ciofs3":
                # time_range = ["1999-1-1","2002-1-1"]
                # time_range = ["2006-1-1","2011-1-1"]
                time_range = ["2014-1-1","2021-1-1"]
            else:
                raise ValueError(f"Unknown model: {model}")

            kwargs_plot = {"model_label": model.upper()}

            project_name = f"{slug}_{model}"

            for key_variable in key_variables: 
                if key_variable not in cat[source_name].metadata["key_variables"]:
                    continue

                if key_variable == "ssh":
                    no_Z = True
                    plot_descriptions_long = [f"Subtidal sea surface height with mean subtracted, from fixed station",
                                         f"Sea surface height with mean subtracted, from fixed station",
                                        ]
                    ts_mods_long = [
                                [{"function": subtract_mean, "inputs": dict(varname=key_variable), "name_mod": "subtract-mean"},
                                    # {"function": oceans.filters.pl33tn, "inputs": dict(mode="same"), "name_mod": "subtidal"}]
                                   {"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",}],]
                    ts_mods_long += [[{"function": subtract_mean, "inputs": dict(varname=key_variable), "name_mod": "subtract-mean"},]]
                    plot_descriptions_short = [
                                         f"Sea surface height with mean subtracted, from fixed station",
                                        ]
                    ts_mods_short = [[{"function": subtract_mean, "inputs": dict(varname=key_variable), "name_mod": "subtract-mean"},]]
                elif key_variable in ["temp"]:
                    no_Z = False

                    # time series for modification
                    df = cat[source_name].read()
                    
                    # try:
                    #     df.cf["T"].dt
                    # except AttributeError:
                    #     import pdb; pdb.set_trace()
                        

                    try:
                        df[df.cf["T"].name] = pd.to_datetime(df.cf["T"])
                        mmean = df.cf[key_variable].groupby(df.cf["T"].dt.month).mean()
                    except ValueError:
                        import pdb; pdb.set_trace()

                    plot_descriptions_long = [f"Subtidal sea temperature, from fixed station",
                                         f"Subtidal sea temperature with mean climatology subtracted, from fixed station",
                                         f"Sea temperature, from fixed station",
                                        ]
                    ts_mods_long = [[
                        # {"function": oceans.filters.pl33tn, "inputs": dict(mode="same"), "name_mod": "subtidal",},
                        {"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",},
                                   ]]
                    ts_mods_long += [[
                        # {"function": oceans.filters.pl33tn, "inputs": dict(mode="same"), "name_mod": "subtidal",},
                        {"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",},
                        {"function": omsa.utils.calculate_anomaly,"inputs": dict(monthly_mean=mmean, varname=key_variable), "name_mod": "subtract-monthly-mean"},
                        ]]
                    # ts_mods_long += [[
                    #     {"function": omsa.utils.calculate_anomaly,"inputs": dict(monthly_mean=mmean), "name_mod": "subtract-monthly-mean"},
                    #                ]]
                    ts_mods_long += [[
                                   ]]
                    plot_descriptions_short = [f"Subtidal sea temperature, from fixed station",
                                         f"Sea temperature, from fixed station",
                                        ]
                    ts_mods_short = [[
                        # {"function": oceans.filters.pl33tn, "inputs": dict(mode="same"), "name_mod": "subtidal",},
                    {"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",},
                    ]]
                    ts_mods_short += [[
                                   ]]
                elif key_variable in ["salt"]:
                    no_Z = False

                    # time series for modification
                    df = cat[source_name].read()
                    # mmean = df.cf[key_variable].groupby(df.cf["T"].month).mean()
                    df[df.cf["T"].name] = pd.to_datetime(df.cf["T"])
                    mmean = df.cf[key_variable].groupby(df.cf["T"].dt.month).mean()
                    plot_descriptions_long = [f"Subtidal salinity, from fixed station",
                                         f"Subtidal salinity with mean climatology subtracted, from fixed station",
                                         f"Salinity, from fixed station",
                                        ]
                    ts_mods_long = [[{"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",},
                                   ]]
                    ts_mods_long += [[{"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",},
                        {"function": omsa.utils.calculate_anomaly,"inputs": dict(monthly_mean=mmean, varname=key_variable), "name_mod": "subtract-monthly-mean"},
                                   ]]
                    ts_mods_long += [[
                                   ]]
                    plot_descriptions_short = [f"Subtidal salinity, from fixed station",
                                         f"Salinity, from fixed station",
                                        ]
                    ts_mods_short = [[{"function": subtidal_dataset, "inputs": dict(varname=key_variable), "name_mod": "subtidal",},]]
                    ts_mods_short += [[
                                   ]]

                kwargs = dict(project_name=project_name, catalogs=cat, model_name=cat_model,
                             preprocess=True,
                             vocabs=cic.utils.vocab,
                            #  vocabs=chr.vocab, 
                             mode="a",
                             key_variable=key_variable, 
                             alpha=5, dd=5, 
                             interpolate_horizontal=False,
                             model_source_name=model,
                             catalog_source_names=[source_name],
                             model_only=False,
                             # user_min_time=start_time_use, user_max_time=end_time_use,
                             check_in_boundary=False,
                             
                             want_vertical_interp=want_vertical_interp,
                             want_locstreamZ=want_locstreamZ,
                             need_xgcm_grid=need_xgcm_grid,
                             kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True),
                    # override_chunks=override_chunks,
                    
                             # ts_mods=ts_mods,
                             plot_map=False,
                             no_Z=no_Z,
                             wetdry=wetdry,
                             plot_count_title=False,
                             vocab_labels="vocab_labels",
                              kwargs_plot=kwargs_plot,
                              known_model_depth_attr_positive="up",
                         override_processed=False,
                         override_stats=False,
                         override_plot=False,
                             )

                start_time = cat[source_name].metadata["minTime"].replace("Z","")
                # this is to skip to the newly available model output
                if start_time < "1999-01-01":
                    start_time = "1999-01-01"
                end_time = cat[source_name].metadata["maxTime"].replace("Z","")
                start_time, end_time = pd.Timestamp(start_time), pd.Timestamp(end_time)

                # For ssh, do subtidal comparison for time series > 35 days in 1 year chunks, otherwise just regular time series comp
                # I don't think there are temp time series that are shorter than 35 days
                if (pd.Timestamp(end_time) - pd.Timestamp(start_time) > pd.Timedelta("365 days")):# or (source_name == "wmo_46077"):

                    dates = pd.date_range(start_time, end_time, freq="1YS", normalize=True)
                    # check to see if start_time is not included by more than a day, since date_range
                    # might have excluded it
                    # import pdb; pdb.set_trace()
                    if start_time + pd.Timedelta("1 day") < dates[0]:
                        dates = pd.date_range(start_time - pd.Timedelta("52W"), end_time, freq="1YS", normalize=True)

                    # dates = pd.date_range(start_time, end_time, freq="12MS")
                    for i, date in enumerate(dates[:-1]):
                        start_time_use, end_time_use = date, dates[i+1]

                        # this is set special since time range for model is limited
                        if end_time_use > pd.Timestamp(time_range[1]):
                            print(f"{end_time_use} is after model output is available {time_range[1]}, skipping")
                            continue
                        if start_time_use < pd.Timestamp(time_range[0]):
                            print(f"{start_time_use} is before model output is available {time_range[0]}, skipping")
                            continue


                        for ts_mod, plot_description in zip(ts_mods_long, plot_descriptions_long):
                            more_kwargs = dict(user_min_time=start_time_use, user_max_time=end_time_use,
                                               plot_description=plot_description,
                                               ts_mods=ts_mod,)

                            omsa.run(**kwargs, **more_kwargs)

                else:
                    for ts_mod, plot_description in zip(ts_mods_short, plot_descriptions_short):
                        more_kwargs = dict(ts_mods=ts_mod,plot_description=plot_description,)
                        omsa.run(**kwargs, **more_kwargs)

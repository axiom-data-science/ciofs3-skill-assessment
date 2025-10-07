"""This runs everything for HF Radar data:
* mean east and north component comparisons with data
* animations of velocity comparisons with data
* It also, importantly, run time series processing files that are used in the other scripts.

Then you should also run the scripts:
* Skill score surface plots -> plot_hfradar_ss.py
* Tidal ellipses and tidal constant plots -> plot_tidal_ellipses.py

"""



import ocean_model_skill_assessor as omsa
# import ciofs_hindcast_report as chr
import intake
import cf_xarray as cfx
import cf_pandas as cfp

# import model_catalogs as mc
import xarray as xr
import pandas as pd

import extract_model as em
import xroms
import oceans.filters
import cmocean.cm as cmo
import cook_inlet_catalogs as cic


cat_model = intake.open_catalog("models.yaml")

slug = "hfradar"
cat = intake.open_catalog(cic.utils.cat_path(slug))
cat.metadata["name"] = slug
# models = ["ciofs_hindcast"]
models = ["ciofs3"]

# test this:
# 2 step process: 
# 1. run to cache model output and variables individually east, north with model_only=True
# 2. run to create quiver figures with model_only=False (other things can be turned off too?)

# time_range = ["2003-1-1","2007-1-1"] 
locstream = False
known_model_depth_attr_positive = "up"
override_chunks = {"ocean_time": -1, "time": -1}
override_processed = False
override_stats = False
override_plot = False


# key_variable = [{"data": ["east","north"], "accessor": "xroms", "function": "eastnorth",},]
# key_variable = [[{"data": ["east", "north"], "accessor": "xroms", "function": "_uv2eastnorth",},]]
key_variables = [
    # {"data": ["east", "north"], "accessor": "xroms", "function": "eastnorth",},
    
    # # correct options, when model caching:
    # [{"data": "east", "accessor": "xroms", "function": "east",}],
    # [{"data": "north", "accessor": "xroms", "function": "north",}]
    # when model caching done:
    ["east", "north"],
    ]

model_only = False

# MOVE TO DICT OPTIONS
# key_variable=["east","north"]
# key_variable = "M2-major"
skip_key_variable_check = True
# skip_key_variable_check = False

override_mask_lon = "lon_rho"
horizontal_interp_code = "xesmf"

xcmocean_options=dict(divin={'along': cmo.delta, 'east': cmo.delta, 'north': cmo.delta}, 
                      regexin={'along': 'along', "east": "east", "north": "north", "speed": "speed"}, 
                      seqin={'along': cmo.speed, 'east': cmo.speed, 'north': cmo.speed},
                      )

# define ts_mods


# calculate weekly averages
def resample(ds, period):
    with xr.set_options(keep_attrs=True):
        tkey = ds.cf["T"].name
        ds_mean = ds.resample({tkey: period}, skipna=True).mean().squeeze()
        ds_mean[tkey].attrs = ds[tkey].attrs
        # import pdb; pdb.set_trace()
        return ds_mean.dropna(dim=ds_mean.cf["T"].name, how="all")
    # return ds.resample(ds.cf["T"].name="1W").mean().squeeze()

def mean(ds):
    tkey = ds.cf["T"].name
    ds_mean = ds.mean(dim=tkey).squeeze()
    # need something in T since required plut good for tracking
    ds_mean[tkey] = ds.cf["T"][0]  # start time
    ds_mean[tkey].attrs = ds[ds.cf["T"].name].attrs
    ds_mean[tkey].attrs["axis"] = "T"
    name_addition = f"averaged from {str(ds.cf['T'][0].values)[:16]} to {str(ds.cf['T'][-1].values)[:16]}"
    if "long_name" in ds_mean[ds.cf["T"].name].attrs:
        ds_mean[tkey].attrs["long_name"] += name_addition
    else:
        ds_mean[tkey].attrs["long_name"] = name_addition
    ds_mean = ds_mean.assign_coords({tkey: ds_mean[tkey]})
    return ds_mean

# # nan out model locations where data are nan
# def match_nans(ds, dd):
#     ds_vars = [var for var in list(ds.data_vars) if ds[var].ndim >= 3]
#     inds = (~dd[list(dd.data_vars)[0]].isnull()).values
#     ds_masked = ds[ds_vars].where(inds) 
#     return ds_masked

# calculate where there are enough data points to consider the location from the data
def remove_under_50_percent_data(ds, dd):
    import numpy as np
    # import pdb; pdb.set_trace()
    ds_vars = [var for var in list(ds.data_vars) if ds[var].ndim >= 3]
    
    # only use points where > 50% presence data
    enough = (~dd[list(dd.data_vars)[0]].isnull()).sum(dim=dd.cf["T"].name)/dd.cf["T"].size
    enough = enough>0.5

    ds_masked = xr.where(enough.values, ds[ds_vars], np.nan, keep_attrs=True)
    ds_masked = ds_masked.transpose(ds.cf["T"].name, ...)

    # add back in coords that disappeared
    coord_diff = list(set(ds.coords) - set(ds_masked.coords))
    if len(coord_diff) == 1:
        ds_masked[coord_diff[0]] = ds[coord_diff[0]]
    return ds_masked

# change units
def cm2m(ds):
    for var in list(ds.data_vars):
        if ds[var].ndim > 2 and "cm" in ds[var].attrs["units"]:
            ds[var] /= 100
            ds[var].attrs["units"] = ds[var].attrs["units"].replace("cm","m")
            ds[var].attrs["long_name"] = ds[var].attrs["long_name"].replace("cm","m")
    return ds

# apply subtidal filter across dataset
def subtidal_dataset(ds):
    import cf_xarray
    for var in list(ds.data_vars):
        # apply to variable in Dataset if it has Time
        if len(cf_xarray.accessor._get_all(ds[var], "T")) > 0:
            # import pdb; pdb.set_trace()
            dim = list(set(override_chunks.keys()).intersection(ds[var].dims))[0]
            ds[var] = oceans.filters.pl33tn(ds[var].chunk(chunks=override_chunks[dim]), mode="same")
    return ds

import cartopy

inputs_dict = {}
inputs_dict["lower-ci_system-B_2006-2007"] =  {"figsize": (15,8), "extent": (-153.05, -151.7, 59.1, 60.0),
                                                   "indexer": {"X": slice(None,None,1), "Y": slice(None, None, 1)},
                                                #    "user_min_time": "2006-11-12T00", "user_max_time": "2007-01-01T00",
                                                   }
# inputs_dict["upper-ci_system-A_2002-2003"] = {"figsize": (15,8), 
#                                              "indexer": {"X": slice(None,None,3), "Y": slice(None, None, 3)},
#                                                  "extent": (-152.15, -151.2, 60.2, 60.8),
#                                                 #  "user_min_time": "2003-01-01T00", "user_max_time": "2003-06-09T20",
#                                                  }
inputs_dict["upper-ci_system-A_2009"] = {"figsize": (15,8), 
                                             "indexer": {"X": slice(None,None,3), "Y": slice(None, None, 3)},
                                                 "extent": (-152.15, -151.2, 60.2, 60.8),
                                                #  "user_min_time": "2003-01-01T00", "user_max_time": "2003-06-09T20",
                                                 }

ref_dict = {}
ref_dict["lower-ci_system-B_2006-2007"] =  {
                                                #    "user_min_time": "2007-10-01T00", "user_max_time": "2007-11-11T00",
                                                #    "user_min_time": "2007-09-01T00", "user_max_time": "2007-10-01T00",
                                                #    "user_min_time": "2007-08-01T00", "user_max_time": "2007-09-01T00",
                                                #    "user_min_time": "2007-07-01T00", "user_max_time": "2007-08-01T00",
                                                #    "user_min_time": "2007-06-01T00", "user_max_time": "2007-07-01T00",
                                                #    "user_min_time": "2007-05-01T00", "user_max_time": "2007-06-01T00",
                                                #    "user_min_time": "2007-04-01T00", "user_max_time": "2007-05-01T00",
                                                #    "user_min_time": "2007-03-01T00", "user_max_time": "2007-04-01T00",
                                                #    "user_min_time": "2007-02-01T00", "user_max_time": "2007-03-01T00",
                                                #    "user_min_time": "2007-01-01T00", "user_max_time": "2007-02-01T00",
                                                   "user_min_time": "2006-11-12T00", "user_max_time": "2007-11-11T00",
                                                   }
ref_dict["upper-ci_system-A_2002-2003"] = {
#                                                  "user_min_time": "2002-12-08T00", "user_max_time": "2003-06-09T20",
                                                 "user_min_time": "2002-12-08T00", "user_max_time": "2003-06-15T00",
                                                 }
ref_dict["upper-ci_system-A_2009"] = {
                                                 "user_min_time": "2009-04-19T00", "user_max_time": "2009-06-07T00",
                                                 }

plots = {}
plots["lower-ci_system-B_2006-2007"] =        {
                                                   "subtidal-mean": {
                                                    #    "scale": 0.00005, 
                                                                     "legend_arrow_length": 0.1, 
                                                                    },
                                                   "hourly-tidal": {
                                                       "scale": 0.0003, 
                                                                     "legend_arrow_length": 1, 
                                                                     "subplot_description": "Surface currents",
                                                                    },
                                                   "6hourly-subtidal": {
                                                       "scale": 0.0003, 
                                                                     "legend_arrow_length": 1, 
                                                                     "subplot_description": "Subtidal surface currents averaged over 6 hours",
                                                                    },
                                                 }
# plots["upper-ci_system-A_2002-2003"] =        {
#                                                    "hourly-tidal": {
#                                                        "scale": 0.0008,  
#                                                                      "legend_arrow_length": 2,  
#                                                                      "subplot_description": "Surface currents",
#                                                                     },
#                                                    "6hourly-subtidal": {
#                                                        "scale": 0.0008, 
#                                                                      "legend_arrow_length": 2, 
#                                                                      "subplot_description": "Subtidal surface currents averaged over 6 hours",
#                                                                     },
#                                                    "subtidal-mean": {
#                                                        "scale": 0.00015, 
#                                                                      "legend_arrow_length": 0.1,  #0.5, 
#                                                                     },
#                                                  }
plots["upper-ci_system-A_2009"] =        {
                                                   "hourly-tidal": {
                                                       "scale": 0.0008,  
                                                                     "legend_arrow_length": 2,  
                                                                     "subplot_description": "Surface currents",
                                                                    },
                                                   "6hourly-subtidal": {
                                                       "scale": 0.0008, 
                                                                     "legend_arrow_length": 2, 
                                                                     "subplot_description": "Subtidal surface currents averaged over 6 hours",
                                                                    },
                                                   "subtidal-mean": {
                                                       "scale": 0.00015, 
                                                                     "legend_arrow_length": 0.1,  #0.5, 
                                                                    },
                                                 }

plot_descriptions = {}
plot_descriptions["lower-ci_system-B_2006-2007"] = "Subtidal surface currents averaged 2006-11-12 to 2007-11-11"
# plot_descriptions["lower-ci_system-B_2006-2007"] = "Subtidal surface currents averaged 2006-11-12 to 2007-01-01"
# plot_descriptions["upper-ci_system-A_2002-2003"] = "Subtidal surface currents averaged 2003-01-01 to 2003-06-09"
plot_descriptions["upper-ci_system-A_2002-2003"] = "Subtidal surface currents averaged 2002-12-08 to 2003-06-15"
plot_descriptions["upper-ci_system-A_2009"] = "Subtidal surface currents averaged 2009-04-19 to 2009-06-07"

ts_mods = {}
ts_mods["hourly-tidal"] = [
                    {"function": remove_under_50_percent_data, "inputs": dict(include_data=True), "name_mod": "remove-under-50-percent-data"},
                    {"function": cm2m, "inputs": dict(), "name_mod": "units-to-meters"},
                          ]
ts_mods["6hourly-subtidal"] = [
                    {"function": remove_under_50_percent_data, "inputs": dict(include_data=True), "name_mod": "remove-under-50-percent-data"},
                    {"function": cm2m, "inputs": dict(), "name_mod": "units-to-meters"},
                    {"function": subtidal_dataset, "inputs": dict(), "name_mod": "subtidal",},
                    {"function": resample, "inputs": dict(period="6H"), "name_mod": "resample-6H"},
                          ]
ts_mods["subtidal-mean"] = [
            {"function": remove_under_50_percent_data, "inputs": dict(include_data=True), "name_mod": "remove-under-50-percent-data"},
    {"function": cm2m, "inputs": dict(), "name_mod": "units-to-meters"},
    {"function": subtidal_dataset, "inputs": dict(), "name_mod": "subtidal",},
    {"function": mean, "inputs": dict(), "name_mod": "mean"},
          ]

# plot_description = "Subtidal surface currents averaged over dataset"

kwargs_plot = dict(
    make_movie=True,
                   proj=cartopy.crs.LambertAzimuthalEqualArea(central_longitude=-151, central_latitude=58),
                                 )

for key_variable in key_variables:
    for model in models:
        project_name = f"{slug}_{model}"
        
        for source_name in inputs_dict:
        # for source_name in ["upper-ci_system-A_2002-2003"]:#inputs_dict:
            
            start_time_use = ref_dict[source_name]["user_min_time"]
            end_time_use = ref_dict[source_name]["user_max_time"]
            
            kwargs_plot.update(inputs_dict[source_name])
            kwargs_plot.update({"model_title": model.upper()})
            for plot in plots[source_name]:
                # if plot != "6hourly-subtidal":
                #     continue
                kwargs_plot_loop = kwargs_plot
                kwargs_plot_loop.update(plots[source_name][plot])
                
                ts_mod = ts_mods[plot]
                # import pdb; pdb.set_trace()
                omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                        preprocess=True,
                        vocabs=cic.utils.vocab,
                        mode="a",
                        key_variable=key_variable, 
                        alpha=5, dd=5, 
                        interpolate_horizontal=True,
                        want_vertical_interp=False,
                        extrap=False,
                        model_source_name=model,
                        catalog_source_names=[source_name],
                        model_only=model_only,
                        user_min_time=start_time_use, user_max_time=end_time_use,
                        check_in_boundary=False,
                        need_xgcm_grid=True,
                        vocab_labels="vocab_labels",
                        plot_map=False,
                        plot_count_title=False,
                        ts_mods=ts_mod,
                        kwargs_plot=kwargs_plot_loop,
                        skip_key_variable_check=skip_key_variable_check,
                        plot_description=plot_descriptions[source_name],
                        
                        override_plot=override_plot,
                        override_processed=override_processed,
                        override_stats=override_stats,
                        xcmocean_options=xcmocean_options,
                        
                        override_mask_lon=override_mask_lon,
                        locstream=locstream,
                        horizontal_interp_code=horizontal_interp_code,
                        known_model_depth_attr_positive=known_model_depth_attr_positive,
                        # override_chunks=override_chunks,
                        )

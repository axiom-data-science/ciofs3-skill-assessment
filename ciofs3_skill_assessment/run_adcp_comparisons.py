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

import numpy as np
from sklearn.decomposition import PCA

def calc_pca(dsm2):

    X = xr.concat([dsm2.cf["east"], dsm2.cf["north"]], dim='component').transpose(dsm2.cf["T"].name, ...)
    # X = xr.concat([dsm2.u[:,:,j,i], dsm2.v[:,:,j,i]], dim='component').transpose('ocean_time', ...)
    X_vals = X.values  # shape: (time, 2, depth)
    
    # don't include nans in PCA
    # Step 1: drop all-NaN time steps
    time_mask = np.any(np.isfinite(X_vals), axis=(1,2))
    X_trim = X_vals[time_mask, :, :]

    # Step 2: drop all-NaN depth levels
    depth_mask = np.all(np.isfinite(X_trim), axis=(0,1))
    X_valid = X_trim[:, :, depth_mask]

    # valid_mask = np.all(np.isfinite(X_vals), axis=(1,2))
    # X_vals = X_vals[valid_mask, :, :]

    n_time, _, n_depth = X_valid.shape

    X_flat = X_valid.reshape(n_time, 2 * n_depth)

    pca = PCA(n_components=1)
    # import pdb; pdb.set_trace()
    pca.fit(X_flat)

    pc1 = pca.components_[0]  # shape: (2 * depth,)

    u_eof = pc1[:n_depth]
    v_eof = pc1[n_depth:]

    # Compute dominant direction (in degrees from east)
    theta_rad = np.arctan2(np.mean(v_eof), np.mean(u_eof))
    theta_deg = np.degrees(theta_rad)

    # print(f"Dominant flow direction at (i={i}, j={j}): {theta_deg:.2f}° from north")
    return theta_deg

def rotate_to_dominant_direction(dsm2):
    """
    
    Notes
    -----
    the rotated u and v variables replace the original u and v variables in the dataset
    so that OMSA can find them. Metadata is properly updated to indicate the rotation angle.
    
    which: str
        "data" or "model"
    """
    # import pdb; pdb.set_trace()
    try:
        theta_deg = calc_pca(dsm2)
        reference = "xaxis"
        # theta_deg = 349
        # reference = "compass"
        dsm2[dsm2.cf["east"].name].attrs["name"] = "east"
        dsm2[dsm2.cf["east"].name].attrs["long_name"] = "eastward velocity m/s"
        dsm2[dsm2.cf["north"].name].attrs["name"] = "north"
        dsm2[dsm2.cf["north"].name].attrs["long_name"] = "northward velocity m/s"
        urot, vrot = xroms.vector.rotate_vectors(dsm2.cf["east"].fillna(0), dsm2.cf["north"].fillna(0), theta_deg, isradians=False, reference=reference)
        # urot, vrot = xroms.vector.rotate_vectors(dsm2.cf["east"], dsm2.cf["north"], theta_deg, isradians=False, reference='compass')
        # urot, vrot = xroms.vector.rotate_vectors(dsm2.cf["east"][:,:,j,i], dsm2.cf["north"][:,:,j,i], theta_deg, isradians=False, reference='compass')
        urot.attrs["angle_degrees_xaxis"] = theta_deg
        vrot.attrs["angle_degrees_xaxis"] = theta_deg
        dsm2[dsm2.cf["east"].name] = urot
        dsm2[dsm2.cf["north"].name] = vrot
        
    except ValueError:
        dsm2[dsm2.cf["east"].name] = dsm2.cf["east"]*np.nan
        dsm2[dsm2.cf["north"].name] = dsm2.cf["north"]*np.nan
        dsm2[dsm2.cf["east"].name].attrs["angle_degrees_xaxis"] = np.nan
        dsm2[dsm2.cf["north"].name].attrs["angle_degrees_xaxis"] = np.nan
    
    # drop unused dims
    unused_dims = set(dsm2.dims) - set(dim for var in dsm2.data_vars.values() for dim in var.dims)
    dsm2 = dsm2.drop_dims(unused_dims)

    return dsm2


def select_variables(ds, var_list):
    # import pdb; pdb.set_trace()
    ds.xroms._uv2eastnorth()
    ds['east'] = ds.xroms.east
    ds['north'] = ds.xroms.north

    speed = ds.xroms.speed
    ds["speed"] = speed
    
    return ds[var_list]#.chunk({"s_rho": 30})


cat_model = intake.open_catalog("models.yaml")


slugs = [
    # "adcp_moored_noaa_coi_other",
    # "adcp_moored_noaa_coi_2005",
 'adcp_moored_noaa_kod_1',
#  'adcp_moored_noaa_kod_2',
 ]

# run for both models
models = ["ciofs3" ]
# models = ["ciofs_fresh"]
# models = ["ciofs_hindcast"]#, "ciofs_fresh"]
# key_variables=["speed","along","across"]


# Need key_variables as dict to have select_variables run which winnows the horizontal grid down to one for u and v for model
# then use ts_mods to rotate to the dominant direction and in some cases apply subtidal filter


# ds.xroms.east_rotated(angle=-90, reference="compass", isradians=False, name="along_channel")
key_variables = [[
                
                
                # These are the ones to use:
                {"data": "east", "function": select_variables, "inputs": dict(var_list=["east", "north", "speed"])},
                # {"data": "north", "function": select_variables, "inputs": dict(var_list=["east", "north", "speed"])},
                # {"data": "speed", "function": select_variables, "inputs": dict(var_list=["east", "north", "speed"])},


                  ]]


if key_variables[0][0]["data"] == "speed":
    vardescs = ["Horizontal Speed"]
elif key_variables[0][0]["data"] == "east":
    vardescs = ["Along-Channel Velocity"]
elif key_variables[0][0]["data"] == "north":
    vardescs = ["Across-Channel Velocity"]


skip_key_variable_check = True
model_only = False
override_mask_lon = "lon_rho"
need_xgcm_grid=True
kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True)
override_chunks = {"s_rho": 30, "s_w": 31}

# use wetdry False to force the use of mask_rho since ADCP would be put out
# where there is no wetting/drying
wetdry = False

# apply subtidal filter across dataset
def subtidal_dataset(ds):
    import cf_xarray
    # import pdb; pdb.set_trace()
    if isinstance(ds, xr.Dataset):
        for var in list(ds.data_vars):
            # apply to variable in Dataset if it has Time
            if len(cf_xarray.accessor._get_all(ds[var], "T")) > 0:
                ds[var] = oceans.filters.pl33tn(ds[var], mode="same")
    elif isinstance(ds, xr.DataArray) and "T" in ds.cf.axes:
        ds = oceans.filters.pl33tn(ds, mode="same").to_dataset(name=ds.name)

    return ds


ts_mods = [
    [{"function": rotate_to_dominant_direction, "inputs": dict(), "name_mod": "rotate"},
     {"function": subtidal_dataset, "inputs": dict(), "name_mod": "subtidal"}],
          [{"function": rotate_to_dominant_direction, "inputs": dict(), "name_mod": "rotate"}],
          ]
ts_mod_descs = ["Subtidal","Tidal"]
# ts_mod_descs = ["Tidal", "Subtidal"]

xcmocean_options=dict(divin={'east': cmo.delta, 'north': cmo.delta}, 
                      regexin={'east': 'east', 'north':'north'}, 
                      seqin={'east': cmo.speed, 'north': cmo.speed})

vocab = cic.utils.vocab

kwargs_plot = dict(figsize=(20,6))

for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    cat.metadata["name"] = slug

    for model in models:
        project_name = f"{slug}_{model}"
        kwargs_plot.update({"model_title": model.upper()})

        for ts_mod, ts_mod_name in zip(ts_mods, ts_mod_descs):

            for key_variable, vardesc in zip(key_variables,vardescs):
                plot_description = f"{ts_mod_name.capitalize()} {vardesc.lower()} from moored ADCP"
                source_names = list(cat)
                # source_names = ["KOD0941"]
                omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                         preprocess=True,
                         vocabs=vocab,
                        #  vocabs=None,#"general", 
                         mode="a",
                         key_variable=key_variable, 
                         alpha=5, dd=5, 
                         interpolate_horizontal=False,
                         want_vertical_interp=True,
                         model_source_name=model,
                         catalog_source_names=source_names,
                         model_only=model_only,
                         # user_min_time=start_time_use, user_max_time=end_time_use,
                         check_in_boundary=False,
                         need_xgcm_grid=need_xgcm_grid,  
                         kwargs_xroms=kwargs_xroms,
                         ts_mods=ts_mod,
                         plot_map=False,
                         plot_count_title=False,
                         vocab_labels="vocab_labels",
                         xcmocean_options=xcmocean_options,
                         # override_model=False,
                         override_processed=False,
                         override_stats=False,
                         override_plot=False,
                         plot_description=plot_description,
                         kwargs_plot=kwargs_plot,
                         
                         skip_key_variable_check=skip_key_variable_check,
                         override_mask_lon=override_mask_lon,
                         override_chunks=override_chunks,
                         wetdry=wetdry,
                        )

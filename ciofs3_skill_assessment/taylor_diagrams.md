---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: ciofs3-skill-assessment
  language: python
  name: python3
---

```{code-cell} ipython3
from pathlib import Path
import pandas as pd
import seaborn as sns
import xarray as xr
import yaml
# import xroms
import cf_pandas
import matplotlib.pyplot as plt
import numpy as np
import cmocean
import cook_inlet_catalogs as cic

from taylorDiagram import TaylorDiagram
# from stats import compute_root_mean_square_error, compute_correlation_coefficient

import geopandas as gpd
from shapely.geometry import Point

import intake

vocab = {}
vocab["lon"] = {"name": '(?i)^(lon|long|lon_rho|longitude)$'}  # "depth" not "bottom"
vocab["depth"] = {"name": '(?i)^(?!.*bottom)(?=.*depth)'}  # "depth" not "bottom"
vocab['x'] = {'name': '(?i).*x[01].*'}  # x with 0 or 1
vocab['y'] = {'name': '(?i).*y[01].*'}
# vocab['temp_comp'] = {'name': '(?i)^(?!.*(F_|qc|air|dew))(?=.*tem)(?=.*comp)'}
vocab['temp'] = {'name': '(?i)^(?!.*(F_|qc|air|dew|comp|diff))(?=.*tem)'}  # doesn't match temp with "model"
vocab['temp_subtidal'] = {'name': '(?i)^(?!.*(F_|qc|air|dew|comp|diff))(?=.*tem)'}  
vocab['temp_subtidal_subtract_monthly_mean'] = {'name': '(?i)^(?!.*(F_|qc|air|dew|comp|diff))(?=.*tem)'}  # doesn't match temp with "model"
# vocab['salt_comp'] = {'name': '(?i)^(?!.*(F_|qc))(?=.*sal)(?=.*comp)'}
vocab['salt'] = {'name': '(?i)^(?!.*(F_|qc|comp|diff))(?=.*sal)'}
vocab['salt_subtidal'] = {'name': '(?i)^(?!.*(F_|qc|comp|diff))(?=.*sal)'}
vocab['salt_subtidal_subtract_monthly_mean'] = {'name': '(?i)^(?!.*(F_|qc|comp|diff))(?=.*sal)'}
vocab['east'] = {'name': '(?i)^(u)$'}
vocab['east_rotate'] = {'name': '(?i)^(u)$'}
vocab['east_rotate_subtidal'] = {'name': '(?i)^(u)$'}
vocab['north'] = {'name': '(?i)^(v)$'}
vocab['north_rotate'] = {'name': '(?i)^(v)$'}
vocab['north_rotate_subtidal'] = {'name': '(?i)^(v)$'}
vocab['speed'] = {'name': '(?i)^(speed|s)$'}
vocab['speed_rotate'] = {'name': '(?i)^(speed|s)$'}
vocab['speed_rotate_subtidal'] = {'name': '(?i)^(speed|s)$'}
vocab["ssh"] = {"name": "(?i)^(?=.*(sea_surface|surface|height|zeta|ssh))"}  # sea surface height
vocab["ssh_subtidal"] = {"name": "(?i)^(?=.*(sea_surface|surface|height|zeta|ssh))"}  # sea surface height
vocab["ssh_subtidal_subtract_monthly_mean"] = {"name": "(?i)^(?=.*(sea_surface|surface|height|zeta|ssh))"}  # sea surface height

years = [2003, 2004, 2005, 2006, 2012, 2013, 2014]
# years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 
#          2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

cf_pandas.set_options(custom_criteria=vocab)
# cf_xarray.set_options(custom_criteria=vocab)
```

# Setup

```{code-cell} ipython3

slugs = {"ctd_transects": [slug for slug in cic.slugs if "ctd_transects" in slug],
          "ctd_profiles": [slug for slug in cic.slugs if "ctd_profiles" in slug],
          "moorings": [slug for slug in cic.slugs if "moorings" in slug],
          "adcp_moored": [slug for slug in cic.slugs if "adcp_moored" in slug],
          "hfradar": [slug for slug in cic.slugs if "hfradar" in slug]
}
# slugs = {"ctd_transects": ["ctd_transects_barabara_to_bluff_2002_2003",
#                             "ctd_transects_otf_kbnerr",  
#                             "ctd_transects_cmi_kbnerr",  #
#                             "ctd_transects_cmi_uaf", 
#                             "ctd_transects_gwa", #
#                             "ctd_transects_uaf",  # 
#                             ],
#           "ctd_profiles": [  "ctd_profiles_2005_noaa",
#                         "ctd_profiles_kachemack_kuletz_2005_2007",
#                         "ctd_profiles_kb_small_mesh_2006",
#                         ],
#           "moorings": [        
#                         "moorings_aoos_cdip",
#                         "moorings_circac", 
#                         "moorings_kbnerr", 
#                         "moorings_kbnerr_bear_cove_seldovia", 
#                         "moorings_kbnerr_historical",  # 
#                         "moorings_kbnerr_homer",
#                         "moorings_noaa",    
#                         "moorings_uaf",  
#                 ],
#           "adcp_moored": ["adcp_moored_noaa_coi_2005", "adcp_moored_noaa_coi_other"],
#           "hfradar": ["hfradar"]
          
# }
models = [
          "data", "ciofs_hindcast", "ciofs_fresh", "ciofs3"
          ]  # add test model names here
model_names = [
               "Data", "CIOFS hindcast", "CIOFS fresh", "CIOFSv3"
               ]  # add test model names here
model_names = {model: name for model, name in zip(models, model_names)}
variables = {"ctd_transects": ["temp", "salt"],
            "ctd_profiles": ["temp", "salt"],
            # "moorings": ["temp", "salt", "ssh"],
            # "moorings": ["temp", "salt", "ssh", 
            #              "temp", "salt", "ssh"],
            "moorings": ["temp", "salt", "ssh", 
                         "temp", "salt", "ssh",
                         "temp", "salt", "ssh"],
            "adcp_moored": ["speed", "speed", "east", "east", "north", "north"],
            "hfradar": ["east", "north",
                        "east", "north"],
            }
# how to identify files
variable_globs = {"ctd_transects": ["temp", "salt"],
                 "ctd_profiles": ["temp", "salt"],
                #  "moorings": ["temp_????-??-??_????-??-??", "salt_????-??-??_????-??-??", "ssh_????-??-??_????-??-??_subtract-mean"],
                #  "moorings": ["temp_????-??-??_????-??-??", "salt_????-??-??_????-??-??", "ssh_????-??-??_????-??-??_subtract-mean",
                #               "temp_*_subtidal", "salt_*_subtidal", "ssh_*_subtract-mean_subtidal"],
                 "moorings": ["temp_????-??-??_????-??-??", "salt_????-??-??_????-??-??", "ssh_????-??-??_????-??-??_subtract-mean",
                              "temp_*_subtidal", "salt_*_subtidal", "ssh_*_subtract-mean_subtidal",
                              "temp_*_subtidal_subtract-monthly-mean", "salt_*_subtidal_subtract-monthly-mean"],
                 "adcp_moored": ["speed_rotate", "speed_rotate_subtidal", "east_rotate", "east_rotate_subtidal", "north_rotate", "north_rotate_subtidal", ],
                 "hfradar": ["east_*_remove-under-50-percent-data_units-to-meters", "north_*_remove-under-50-percent-data_units-to-meters",
                             "east_*_remove-under-50-percent-data_units-to-meters_subtidal_mean", "north_*_remove-under-50-percent-data_units-to-meters_subtidal_mean"]
                 }
# what to call the columns/variable to differentiate e.g. u and u_subtidal
variable_names = {"ctd_transects": ["temp", "salt"],
                 "ctd_profiles": ["temp", "salt"],
                #  "moorings": ["temp", "salt", "ssh"],
                #  "moorings": ["temp", "salt", "ssh",
                #               "temp_subtidal", "salt_subtidal", "ssh_subtidal"],
                 "moorings": ["temp", "salt", "ssh",
                              "temp_subtidal", "salt_subtidal", "ssh_subtidal",
                              "temp_subtidal_subtract_monthly_mean", "salt_subtidal_subtract_monthly_mean"],
               #   "adcp_moored": ["speed", "speed_subtidal", "along", "along_subtidal", "across", "across_subtidal", ],
                 "adcp_moored": ["speed", "speed_subtidal", "east", "east_subtidal", "north", "north_subtidal", ],
                 "hfradar": ["east", "north",
                             "east_subtidal", "north_subtidal"]
                 }
vardescs = {"temp": "Sea temperature [C]",
           "salt": "Salinity",
           "ssh": "Sea surface height (mean subtracted) [m]",
           "temp_subtidal": "Sea temperature subtidal [C]",
           "salt_subtidal": "Salinity subtidal",
           "ssh_subtidal": "Sea surface height subtidal [m]",
           "temp_subtidal_subtract_monthly_mean": "Sea temperature subtidal\nsubtract monthly mean [C]",
           "salt_subtidal_subtract_monthly_mean": "Salinity subtidal subtract\nmonthly mean",
           "ssh_subtidal_subtract_monthly_mean": "Sea surface height subtidal\nsubtract monthly mean [m]",
           # use these for hfradar
           "east": "East-west current [m/s]",
           "east_subtidal": "East-west subtidal current [m/s]",
           "north": "North-south current [m/s]",
           "north_subtidal": "North-south subtidal current [m/s]",
          # # use these for ADCP
          #  "east": "Along-channel current [m/s]",
          #  "east_subtidal": "Along-channel subtidal current [m/s]",
          #  "north": "Across-channel current [m/s]",
          #  "north_subtidal": "Across-channel subtidal current [m/s]",
          #  "speed": "Speed [m/s]",
          #  "speed_subtidal": "Speed subtidal [m/s]",
           }
```

```{code-cell} ipython3

# Load the GeoJSON file for defining regions (done in `make_regions.py`)
gdf = gpd.read_file("cook_inlet_regions.geojson")

seasons = {"January": "winter", "February": "winter", "March": "winter",
           "April": "spring", "May": "spring",
           "June": "summer", "July": "summer", "August": "summer",
           "September": "fall", "October": "fall", "November": "fall",
           "December": "winter"}

colors_seasons = {"winter": '#0072B2', "summer": '#E69F00', "spring": '#009E73', "fall": '#CC79A7'}
colors_regions = {1: 'tab:blue', 2: 'tab:orange', 3: 'tab:green', 4: 'tab:purple', 5: 'tab:red'}

markers = {"ciofs_hindcast": "*", "ciofs_fresh": "^", "ciofs3": "o"}


alpha = 0.8
```

![](cook_inlet_regions.png)

```{code-cell} ipython3
def get_value(metrics, slug, transect, model, variable, metric):
    return metrics[(metrics["slug"] == slug) & (metrics["transect"] == transect) & (metrics["model"] == model) 
        & (metrics["variable"] == variable) & (metrics["metric"] == metric)].iloc[0]["value"]
    
def load_transects(slug):
    loc = Path("~/projects/cook-inlet-catalogs/cook_inlet_catalogs/catalogs") / f"{slug}.yaml"
    cat = intake.open_catalog(str(loc))
    transects = list(cat)
    return transects


# def load_date_loc(model, slug, transect):
#     # take first variable data file
#     base_comp = Path(f"/home/kristen/.cache/ocean-model-skill-assessor/{slug}_{model}/processed/")
#     path = list(base_comp.glob(f"{slug}_{transect.replace(' ', '_')}_*_data.csv"))[0]

#     try:
#         df = pd.read_csv(path)
#         num = len(df)
#         return df.cf["T"].iloc[int(num/2)], df.cf["longitude"].iloc[int(num/2)], df.cf["latitude"].iloc[int(num/2)]
#     except:
#         print(f"File not found: {path}")
#         return np.nan, np.nan, np.nan

def find_polygon(lon, lat):
    point = Point(lon, lat)
    match = gdf[gdf.contains(point)]
    if not match.empty:
        return match.iloc[0]
    else:

        distances = gdf.distance(point)
        closest_idx = distances.idxmin()
        closest_region = gdf.loc[closest_idx]
        return closest_region
```

# taylor diagram from processed data

## define data functions

### first

```{code-cell} ipython3

def preprocess(ds):
    # Drop z_rho if present
    if "z_rho" in ds.coords:
        ds = ds.drop_vars("z_rho")
    return ds.squeeze()

def load_data(slug, transect, model, variable, variable_glob):
    """load processed data and model output
    
    variable: "salt" or "temp"
    """


    # data can come from either model and will be the same so choose one
    if model == "data":
        base_comp = Path(f"/home/kristen/.cache/ocean-model-skill-assessor/{slug}_ciofs3/processed/")
        if "adcp" in slug:
            path = base_comp / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.nc"
            # import pdb; pdb.set_trace()
            try:
                df = xr.open_dataset(path).to_dataframe().reset_index()
                if pd.Timestamp(df.cf["T"].iloc[0]).year not in years:
                    df = None  # skip years that are not in the dataset
            except FileNotFoundError:
                # print(f"File not found: {path}")
                df = None
            except ValueError:
                import pdb; pdb.set_trace()
                
        elif "hfradar" in slug:
            path = base_comp / "shorter_range" / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.nc"
            # if model == "ciofs3":
            #     path = base_comp / "shorter_range" / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.nc"
            # else:
            #     path = base_comp / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.nc"
            if "2009" in path.name:
                return None
            # import pdb; pdb.set_trace()
            try:
                print(f"Loading {path}")
                ds = xr.open_mfdataset(str(path))
                df = ds.to_dataframe().reset_index()
                if pd.Timestamp(df.cf["T"].iloc[0]).year not in years:
                    df = None  # skip years that are not in the dataset
            except FileNotFoundError:
                # print(f"File not found: {path}")
                df = None
            # except ValueError:
            #     import pdb; pdb.set_trace()

        elif "moorings" in slug:
            # path = base_comp / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.csv"
            path = sorted(base_comp.glob(f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.csv"))
            if len(path) == 0:  # skip short deployments for this analysis
                return None
            df = pd.concat([pd.read_csv(f) for f in path], ignore_index=True)
            if df.cf["longitude"].isnull().iloc[0] or df.cf["latitude"].isnull().iloc[0]:
                cat = intake.open_catalog(f"../../cook-inlet-catalogs/cook_inlet_catalogs/catalogs/{slug}.yaml")
                df[df.cf["longitude"].name] = cat[transect].metadata["maxLongitude"]
                df[df.cf["latitude"].name] = cat[transect].metadata["maxLatitude"]
                # import pdb; pdb.set_trace()
            

        else:
            path = base_comp / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_data.csv"
        
            try:
                df = pd.read_csv(path)
                if pd.Timestamp(df.cf["T"].iloc[0]).year not in years:
                    df = None  # skip years that are not in the dataset
            except FileNotFoundError:
                # print(f"File not found: {path}")
                df = None
        # if df is not None:
        #     print(f"Loaded data for {slug} {transect} {variable} from {path}")
            
    else:
        base_comp = Path(f"/home/kristen/.cache/ocean-model-skill-assessor/{slug}_{model}/processed/")
        path = base_comp / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_model.nc"
        
        if "hfradar" in slug:
            if model == "ciofs3":
                path = base_comp / "shorter_range" / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_model.nc"
            else:
                path = base_comp / f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_model.nc"
            if "2009" in path.name:
                return None
            # import pdb; pdb.set_trace()
            try:
                print(f"Loading {path}")
                ds = xr.open_mfdataset(str(path))
                if model == "ciofs3":
                    if (abs(ds[variable]) > 100).sum().values > 0:
                        ds[variable] = ds[variable].where(abs(ds[variable]) < 100)
                    # import pdb; pdb.set_trace()
                # # replace values over 1e36 with nan
                # ds = ds.where(ds < 1e36, drop=True)
                df = ds.to_dataframe().reset_index()
                if pd.Timestamp(df.cf["T"].iloc[0]).year not in years:
                    df = None  # skip years that are not in the dataset
            except FileNotFoundError:
                # print(f"File not found: {path}")
                df = None
        elif "moorings" in slug:
            def drop_bad_coords(ds):
                return ds.drop_vars(["z_rho", "xi_rho", "eta_rho"])
                # return ds.drop_vars(["z_rho", "xi_rho", "eta_rho"], errors="ignore")
            # if slug == "moorings_noaa":
            #     import pdb; pdb.set_trace()
            path = sorted(base_comp.glob(f"{slug}_{transect.replace(' ', '_')}_{variable_glob}_model.nc"))
            year_strings = [f"{year}-01-01_{year+1}-01-01" for year in years]
            path = [p for p in path if any(ys in p.name for ys in year_strings)]
            # path = [p for p in path if "2003-01-01_2004-01-01" in p.name or "2004-01-01_2005-01-01" in p.name or "2005-01-01_2006-01-01" in p.name \
            #                         or "2006-01-01_2007-01-01" in p.name or "2012-01-01_2013-01-01" in p.name or "2013-01-01_2014-01-01" in p.name \
            #                             or "2014-01-01_2015-01-01" in p.name]
            if len(path) == 0:  # skip short deployments for this analysis
                return None
            try:
                print(f"Loading {path}")
                
                ds = xr.open_mfdataset(path, preprocess=preprocess, coords='minimal', compat='override')
                # ds = xr.open_mfdataset(path, combine='by_coords', preprocess=drop_bad_coords,)
                df = ds.to_dataframe().reset_index()
                # if pd.Timestamp(df.cf["T"].iloc[0]).year not in [2003, 2004, 2005, 2006, 2012, 2013, 2014]:
                #     df = None  # skip years that are not in the dataset
            except FileNotFoundError:
                print(f"File not found: {path}")
                df = None
            except:
                print(f"Error loading {path}")
                df = None
                import pdb; pdb.set_trace()
        else:
            try:
                ds = xr.open_dataset(path)
                df = ds.to_dataframe().reset_index()
                if pd.Timestamp(df.cf["T"].iloc[0]).year not in years:
                    df = None  # skip years that are not in the dataset
            except FileNotFoundError:
                # print(f"File not found: {path}")
                df = None
        # if df is not None:
        #     print(f"Loaded model data for {slug} {transect} {variable} from {path}")

    return df

def get_transects(slug):        
    loc = Path("~/projects/cook-inlet-catalogs/cook_inlet_catalogs/catalogs") / f"{slug}.yaml"
    cat = intake.open_catalog(str(loc))
    transects = list(cat)
    for transect in transects:
        if "moorings" not in slug:
            if pd.Timestamp(cat[transect].metadata["minTime"]).year not in years or \
            pd.Timestamp(cat[transect].metadata["maxTime"]).year not in years:
                transects.remove(transect)

    if slug == "hfradar":
        # no 2009 bc no CIOFS fresh for that year
        transects = ['lower-ci_system-B_2006-2007','upper-ci_system-A_2002-2003']
        # transects = ['lower-ci_system-B_2006-2007','upper-ci_system-A_2002-2003','upper-ci_system-A_2009']
        # transects = ['lower-ci_system-B_2006_subtidal_daily_mean', 'lower-ci_system-B_2006_subtidal_weekly_mean', 'lower-ci_system-B_2006_tidecons', 
        #              'upper-ci_system-A_2003_subtidal_daily_mean', 'upper-ci_system-A_2003_subtidal_weekly_mean', 'upper-ci_system-A_2003_tidecons',
        #              'upper-ci_system-A_2009', 'upper-ci_system-A_2009_subtidal_weekly_mean', 'upper-ci_system-A_2009_tidecons']
    
    return transects
```

### second

```{code-cell} ipython3
def gather_data(data_type):
    df = {}
    for variable, variable_glob, variable_name in zip(variables[data_type], variable_globs[data_type], variable_names[data_type]):
        print(variable_name)
        df[variable_name] = {"winter": [], "spring": [], "summer": [], "fall": [],
                    1: [], 2: [], 3: [], 4: [], 5: []}
        for slug in slugs[data_type]:
            print(f"Processing {slug}...")
            for transect in get_transects(slug):
                dfsave = pd.DataFrame()
                season, region = None, None
                for model in models:
                    dftemp = load_data(slug, transect, model, variable, variable_glob)
                    # import pdb; pdb.set_trace()
                    if dftemp is None:
                        continue
                    
                    # find season and region to put in correct which
                    dftemp[dftemp.cf["T"].name] = pd.to_datetime(dftemp.cf["T"])
                    date = pd.Timestamp(dftemp.cf["T"].iloc[0])
                    season = seasons[date.month_name()]
                    try:
                        region = find_polygon(dftemp.cf["longitude"].iloc[0], dftemp.cf["latitude"].iloc[0])["region_id"]
                    except KeyError:
                        import pdb; pdb.set_trace()
                    except ValueError:
                        continue
                        # MAY NEED TO REVISIT THIS IF CATCHING TOO MANY ENTRIES
                    
                    # rename columns so they are consistent
                    # if variable == "along_rotate_subtidal":
                    #     import pdb; pdb.set_trace()
                    # import pdb; pdb.set_trace()
                    
                    try:
                        dftemp = dftemp.rename(columns={dftemp.cf["T"].name: "time", dftemp.cf["longitude"].name: "lon", dftemp.cf["latitude"].name: "lat",
                                                dftemp.cf[variable].name: variable_name})
                        # dftemp = dftemp.rename(columns={dftemp.cf["T"].name: "time", dftemp.cf["longitude"].name: "lon", dftemp.cf["latitude"].name: "lat",
                        #                         dftemp.cf[variable].name: variable})
                    except:
                        import pdb; pdb.set_trace()
                    keys = ["time", "lon", "lat", variable_name]
                    # keys = ["time", "lon", "lat", variable]
                    # import pdb; pdb.set_trace()
                    if "Z" in dftemp.cf.keys():
                        dftemp = dftemp.rename(columns={dftemp.cf["Z"].name: "depth"})
                        keys.append("depth")
                    # this is to help keep indices consistent across datasets
                    # let's just drop depth column for SSH since it is handled several ways
                    # but isn't needed for analysis
                    if data_type == "moorings" and "depth" in dftemp:# and "ssh" in variable_name:
                        dftemp = dftemp.drop(columns=["depth"])
                        keys.pop(keys.index("depth"))
                    dftemp = dftemp[keys].copy()
                    dftemp["slug"] = slug
                    dftemp["transect"] = transect
                    
                    colname = f"{model}_{variable_name}"
                    # colname = f"{model}_{variable}"
                    dftemp = dftemp.rename(columns={variable_name: colname})
                    # dftemp = dftemp.rename(columns={variable: colname})
                    # set index to be sure different datasets align
                    indices = ["time"]
                    if "depth" in dftemp and dftemp["depth"].unique().size > 1:
                        indices.append("depth")
                    # dftemp = dftemp.set_index(indices)
                    # import pdb; pdb.set_trace()
                    if dftemp["lon"].unique().size > 1:
                        indices.append("lon")
                    if dftemp["lat"].unique().size > 1:
                        indices.append("lat")
                    dftemp = dftemp.set_index(indices)
                    
                    dftemp_nodup = dftemp[~dftemp.index.duplicated(keep="first")]
                    dftemp_nodup = dftemp_nodup.sort_index()

                    if dfsave.empty:
                        dfsave = dftemp_nodup.copy()
                    else:
                        
                        
                        # Take the union of both time indices
                        # import pdb; pdb.set_trace()
                        combined_index = dftemp_nodup.index.union(dfsave.index)

                        # import pdb; pdb.set_trace() 
                        dfsave[colname] = dftemp_nodup[colname].reindex(combined_index).interpolate(method='linear', limit=10).reindex(dfsave.index)
                        # dfsave = pd.concat([dfsave, dftemp], axis=1, join="outer")
                        # print(dfsave.columns, dftemp.columns, colname)
                        # dfsave[colname] = dftemp_nodup[colname]
                        # dfsave[colname] = (
                        #     dftemp_nodup[colname]
                        #     .reindex(dfsave.index)         # align to dfsave index
                        #     .interpolate(method="linear")  # interpolate missing values
                        # )
                        # dfsave[colname] = dftemp[colname]
                        # import pdb; pdb.set_trace()
                    # try:
                    #     if dfsave.empty:
                    #         dfsave = dftemp.copy()
                    #     else:
                    #         # dfsave = pd.concat([dfsave, dftemp], axis=1, join="outer")
                    #         dfsave[colname] = dftemp[colname]
                    # except:
                    #     import pdb; pdb.set_trace()
                    # drop duplicate columns
                    dfsave = dfsave.loc[:, ~dfsave.columns.duplicated()]

                if season is not None and region is not None:
                    df[variable_name][season].append(dfsave)
                    df[variable_name][region].append(dfsave)
    # concatenate the dataframes for each season and region
    for variable_name in df:
        # print(variable_name)
        for which in df[variable_name]:
            # print(which)
            if len(df[variable_name][which]) > 0:
                # try:
                # # only take variable column
                # dfs_use = [dff.cf[variable_name] for dff in df[variable_name][which] if not dff.empty]
                # # skip full datframe
                # df[variable_name][which] = pd.concat(dfs_use, axis=0)

                # dfs_use = [dff.cf[variable_name] for dff in df[variable_name][which][1:] if not dff.empty]
                # # then combine with one full datframe
                # df[variable_name][which] = pd.concat(df[variable_name][which], pd.concat(dfs_use, axis=0), axis=0)

                try:
                    df[variable_name][which] = pd.concat(df[variable_name][which], axis=0)
                except:
                    import pdb; pdb.set_trace()

                    # # then combine with one full datframe
                    # df[variable_name][which] = pd.concat(df[variable_name][which], pd.concat(dfs_use, axis=0), axis=0)
                # except:
                #     import pdb; pdb.set_trace()
                # # try:
                # #     df[variable_name][which] = pd.concat(df[variable_name][which], axis=0)
                # # except:
                # #     import pdb; pdb.set_trace()
                # # drop duplicate columns
                # df[variable_name][which] = df[variable_name][which].loc[:, ~df[variable_name][which].columns.duplicated()]
            else:
                df[variable_name][which] = pd.DataFrame()

    return df

def remove_nans(df):
    """This remove any columns that have any nan's so that models are accurately compared to each other."""
    
    df_no_nans = {}
    for variable in df:
        df_no_nans[variable] = {}
        for which in df[variable]:
            if not df[variable][which].empty:
                skip_combinations = []
                for model in models:
                    if f"{model}_{variable}" not in df[variable][which].columns:
                        # print(f"{model}_{variable}", df[variable][which].columns)
                        skip_combinations.append(True)
                    else:
                        skip_combinations.append(False)

                if any(skip_combinations):
                    print(f"Skipping {variable} {which} because not all models present")
                    # print("hi")
                    df_no_nans[variable][which] = pd.DataFrame()
                else:
                    # import pdb; pdb.set_trace()
                    df_no_nans[variable][which] = df[variable][which]#.dropna()
            else:
                df_no_nans[variable][which] = pd.DataFrame()
            # if variable == "ssh_subtidal" and which == 5:
            #     import pdb; pdb.set_trace()
            df_no_nans[variable][which] = df_no_nans[variable][which].dropna()
    # import pdb; pdb.set_trace()
    return df_no_nans
```

## define plot functions

```{code-cell} ipython3
def make_td_by_season(df, data_type, data_type_name, srange=(0, 2), plot_var=None, extend=False):

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))

    for ax in axes:
        # Turn off the rectangle (axes[0])
        ax.axis('off')


    refstd = 1 # reference standard deviation

    # if data_type == "adcp_moored":
    if plot_var is not None:
        variable_names_use = [name for name in variable_names[data_type] if plot_var in name]
        variables_use = [var for var in variables[data_type] if plot_var in var]
        # import pdb; pdb.set_trace()
    else:
        variable_names_use = variable_names[data_type]
        variables_use = variables[data_type]

    for variable, variable_name, rect in zip(variables_use, variable_names_use, [121, 122]):
        print(variable_name)
        vardesc = vardescs[variable_name]
        # Taylor diagram
        dia = TaylorDiagram(refstd, fig=fig, rect=rect, label="Reference", extend=extend,
                            srange=srange)
            

        for season in ["winter", "spring", "summer", "fall"]:
            
            color = colors_seasons[season]

            # import pdb; pdb.set_trace()
            try:
                obsstd = df[variable_name][season][f"data_{variable_name}"].std() 
                # obsstd = df[variable_name][season][f"data_{variable}"].std() 
            except KeyError:
                continue
                

            for model in ["ciofs_fresh", "ciofs_hindcast", "ciofs3"]:
                marker = markers[model]
                key = f"{model}_{variable_name}"
                # key = f"{model}_{variable}"
                corr = df[variable_name][season][f"data_{variable_name}"].corr(df[variable_name][season][key])
                # corr = df[variable_name][season][f"data_{variable}"].corr(df[variable_name][season][key])
                # normalize (corr already is)
                std = df[variable_name][season][key].std() 
                stdnorm = std/obsstd
                dia.add_sample(stdnorm, corr, marker=marker, ms=8, alpha=alpha, ls='', color=color)
                print(f"{season} {model} {variable}: std={std:.2f}, obsstd={obsstd:.2f}, stdnorm={stdnorm:.2f}, corr={corr:.2f}")

        # Add grid
        dia.add_grid(lw=0.25)

        # Add RMS contours, and label them
        contours = dia.add_contours(colors='0.5', linewidths=0.5)
        plt.clabel(contours, inline=1, fontsize=10, fmt='%.2f')

        # Tricky: ax is the polar ax (used for plots), _ax is the
        # container (used for layout)
        dia._ax.set_title(f"{vardesc}", pad=30, fontsize=14)

        fig.suptitle(f"{data_type_name} by Season", fontsize=16, y=1.06)

        from matplotlib.lines import Line2D

        legend_elements = []
        # Define custom legend handles
        for season, color in colors_seasons.items():
            # color = colors[match["region_id"]]
            
            # don't show marker if no data
            if df[variable_name][season].empty:
                continue
            
            label = season.capitalize()  # Capitalize the season name
            # label = gdf[gdf["region_id"] == region]["name"].iloc[0]
            legend_elements.append(Line2D([0], [0], marker='o', color='w', label=f"{label}",
                                        markerfacecolor=color, markersize=10, alpha=alpha))
        for model in ["ciofs_fresh", "ciofs_hindcast", "ciofs3"]:
            legend_elements.append(Line2D([0], [0], marker=markers[model], color='w', label=model,
                                        markerfacecolor="0.5", markersize=10, alpha=alpha))


        # Add custom legend
        if data_type == "adcp_moored":
            rect_legend = 121
        else:
            rect_legend = 122
            
        if rect == rect_legend:
            dia._ax.legend(handles=legend_elements, title="Seasons", loc="upper left")
            dia._ax.axis('off')
    plt.show()
    # os.makedirs("figures/taylor_diagrams", exist_ok=True)
    # if data_type == "adcp_moored":
    if plot_var is not None:
        fig.savefig(f"figures/taylor_diagrams/{data_type}_by_season_{plot_var}.png", dpi=300, bbox_inches='tight')
    else:
        fig.savefig(f"figures/taylor_diagrams/{data_type}_by_season.png", dpi=300, bbox_inches='tight')
```

```{code-cell} ipython3
def make_td_by_region(df, data_type, data_type_name, srange=(0, 2), plot_var=None, extend=False, nvars=2):
    
    if nvars == 2:
        figsize = (12, 5.5)
        rects = [121, 122]
    elif nvars == 3:
        figsize = (15, 5.5)
        rects = [131, 132, 133]
    else:
        raise ValueError("nvars must be 2 or 3")

    fig, axes = plt.subplots(1, nvars, figsize=figsize)

    for ax in axes:
        # Turn off the rectangle (axes[0])
        ax.axis('off')

    refstd = 1 # reference standard deviation

    # if data_type == "adcp_moored":
    if plot_var is not None:
        variable_names_use = [name for name in variable_names[data_type] if plot_var in name]
        variables_use = [var for var in variables[data_type] if plot_var in var]
        # import pdb; pdb.set_trace()
    else:
        variable_names_use = variable_names[data_type]
        variables_use = variables[data_type]

    for variable, variable_name, rect in zip(variables_use, variable_names_use, rects):
        print(variable_name)
        vardesc = vardescs[variable_name]

        # Taylor diagram
        dia = TaylorDiagram(refstd, fig=fig, rect=rect, label="Reference", extend=extend,
                            srange=srange)
            

        for region in [1, 2, 3, 4, 5]:
            
            color = colors_regions[region]

            try:
                obsstd = df[variable_name][region][f"data_{variable_name}"].std() 
                # obsstd = df[variable_name][region][f"data_{variable}"].std() 
            except KeyError:
                continue

            for model in ["ciofs_fresh", "ciofs_hindcast", "ciofs3"]:
                marker = markers[model]

                corr = df[variable_name][region][f"data_{variable_name}"].corr(df[variable_name][region][f"{model}_{variable_name}"])
                # corr = df[variable_name][region][f"data_{variable}"].corr(df[variable_name][region][f"{model}_{variable}"])
                # normalize (corr already is)
                std = df[variable_name][region][f"{model}_{variable_name}"].std() 
                # std = df[variable_name][region][f"{model}_{variable}"].std() 
                stdnorm = std/obsstd
                dia.add_sample(stdnorm, corr, marker=marker, ms=8, alpha=alpha, ls='', color=color)
                print(f"{region} {model} {variable}: std={std:.2f}, obsstd={obsstd:.2f}, stdnorm={stdnorm:.2f}, corr={corr:.2f}")

        # Add grid
        dia.add_grid(lw=0.25)

        # Add RMS contours, and label them
        contours = dia.add_contours(colors='0.5', linewidths=0.5)
        plt.clabel(contours, inline=1, fontsize=10, fmt='%.2f')

        # Tricky: ax is the polar ax (used for plots), _ax is the
        # container (used for layout)
        dia._ax.set_title(f"{vardesc}", pad=30, fontsize=14)

        fig.suptitle(f"{data_type_name} by Region", fontsize=16, y=1.06)


        from matplotlib.lines import Line2D

        legend_elements = []
        # Define custom legend handles
        for region, color in colors_regions.items():
            # color = colors[match["region_id"]]
            
            # don't show marker if no data
            if df[variable_name][region].empty:
                continue
            
            label = gdf[gdf["region_id"] == region]["name"].iloc[0]
            # label = gdf[gdf["region_id"] == region]["name"].iloc[0]
            legend_elements.append(Line2D([0], [0], marker='o', color='w', label=f"{label}",
                                        markerfacecolor=color, markersize=10, alpha=alpha))
        for model in ["ciofs_fresh", "ciofs_hindcast", "ciofs3"]:
            legend_elements.append(Line2D([0], [0], marker=markers[model], color='w', label=model,
                                        markerfacecolor="0.5", markersize=10, alpha=alpha))


        # Add custom legend
        if data_type in ["adcp_moored", "hfradar"]:
            rect_legends = [121, 131]
        else:
            rect_legends = [122, 132]
            
        if rect == rect_legends[0] or rect == rect_legends[1]:
            dia._ax.legend(handles=legend_elements, title="Regions", loc="upper left")
            dia._ax.axis('off')


    plt.show()
    # os.makedirs("figures/taylor_diagrams", exist_ok=True)
    # if data_type == "adcp_moored":
    if plot_var is not None:
        fig.savefig(f"figures/taylor_diagrams/{data_type}_by_region_{plot_var}.png", dpi=300, bbox_inches='tight')
    else:
        fig.savefig(f"figures/taylor_diagrams/{data_type}_by_region.png", dpi=300, bbox_inches='tight')
```

## Gather data

+++

### CTD Profiles

```{code-cell} ipython3
data_type = "ctd_profiles"
df_ctd_profiles = gather_data(data_type)
# df_ctd_profiles = remove_nans(df_ctd_profiles)
df_ctd_profiles
```

### CTD Transects

```{code-cell} ipython3
data_type = "ctd_transects"
df_ctd_transects = gather_data(data_type)
# df_ctd_transects = remove_nans(df_ctd_transects)
```

### ADCP

```{code-cell} ipython3
data_type = "adcp_moored"
df_adcp_moored = gather_data(data_type)
# df_adcp_moored
# should use remove_nans but no ADCP years overlap between ciofs fresh and ciofs3 currently
df_adcp_moored = remove_nans(df_adcp_moored)
```

```{code-cell} ipython3
df_adcp_moored = remove_nans(df_adcp_moored)
```

```{code-cell} ipython3
df_adcp_moored["speed"]["summer"]#.dropna(subset=["ciofs_hindcast_speed"])
```

### Moorings

```{code-cell} ipython3
df_moorings["ssh"][1]
```

```{code-cell} ipython3
data_type = "moorings"
df_moorings = gather_data(data_type)
df_moorings = remove_nans(df_moorings)
df_moorings
```

```{code-cell} ipython3
xr.open_mfdataset([path[0]], preprocess=preprocess, coords='minimal', compat='override')
```

```{code-cell} ipython3
xr.open_mfdataset?
```

```{code-cell} ipython3
from pathlib import PosixPath
path = [PosixPath('/home/kristen/.cache/ocean-model-skill-assessor/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/processed/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2004-01-01_2005-01-01_model.nc'), PosixPath('/home/kristen/.cache/ocean-model-skill-assessor/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/processed/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2005-01-01_2006-01-01_model.nc'), PosixPath('/home/kristen/.cache/ocean-model-skill-assessor/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/processed/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2006-01-01_2007-01-01_model.nc'), PosixPath('/home/kristen/.cache/ocean-model-skill-assessor/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/processed/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2012-01-01_2013-01-01_model.nc'), PosixPath('/home/kristen/.cache/ocean-model-skill-assessor/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/processed/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2013-01-01_2014-01-01_model.nc'), PosixPath('/home/kristen/.cache/ocean-model-skill-assessor/moorings_kbnerr_bear_cove_seldovia_ciofs_hindcast/processed/moorings_kbnerr_bear_cove_seldovia_nerrs_kacsdwq_temp_2014-01-01_2015-01-01_model.nc')]
ds = xr.open_mfdataset(path, preprocess=preprocess, coords='minimal', compat='override')
```

### HFRadar

```{code-cell} ipython3
data_type = "hfradar"
df_hfradar = gather_data(data_type)
```

```{code-cell} ipython3
df_hfradar_no_nans = remove_nans(df_hfradar)
```

## run plots

+++

### CTD Profiles

```{code-cell} ipython3
data_type, data_type_name = "ctd_profiles", "CTD Profiles"
srange = (0, 4)
make_td_by_season(df_ctd_profiles, data_type, data_type_name, srange)
make_td_by_region(df_ctd_profiles, data_type, data_type_name, srange)
```

### CTD Transects

```{code-cell} ipython3
data_type, data_type_name = "ctd_transects", "CTD Transects"
srange = (0, 2.4)
make_td_by_season(df_ctd_transects, data_type, data_type_name, srange)
make_td_by_region(df_ctd_transects, data_type, data_type_name, srange)
```

### ADCP

```{code-cell} ipython3
data_type, data_type_name = "adcp_moored", "ADCP Moored"
srange = (0, 1.75)
for key in ["speed", "east", "north"]:
# for key in ["speed_rotate", "east", "north"]:
    make_td_by_region(df_adcp_moored, data_type, data_type_name, srange, plot_var=key, extend=False)
    make_td_by_season(df_adcp_moored, data_type, data_type_name, srange, plot_var=key, extend=False)

# key = "north"  # "east", "north", "speed"
# make_td_by_season(df_adcp_moored, data_type, data_type_name, srange, plot_var=key, extend=False)
# make_td_by_region(df_adcp_moored, data_type, data_type_name, srange, plot_var=key, extend=False)
```

### Moorings

```{code-cell} ipython3
data_type, data_type_name = "moorings", "Moorings"
srange = (0, 2)
for key in ["ssh", "temp", "salt"]:
    if key == "ssh":
        nvars = 2
    else:
        nvars = 3
    make_td_by_region(df_moorings, data_type, data_type_name, srange, plot_var=key, extend=False, nvars=nvars)
```

### HFRadar

```{code-cell} ipython3
data_type, data_type_name = "hfradar", "HFRadar"
srange = (0, 2.5)
# make_td_by_season(df_hfradar, data_type, data_type_name, srange)
for variable in ["east", "north"]:
    make_td_by_region(df_hfradar_no_nans, data_type, data_type_name, srange, plot_var=variable, extend=False)
```

```{code-cell} ipython3
data_type, data_type_name = "hfradar", "HFRadar"
srange = (0, 2.5)
# make_td_by_season(df_hfradar, data_type, data_type_name, srange)
for variable in ["east", "north"]:
    make_td_by_region(df_hfradar, data_type, data_type_name, srange, plot_var=variable, extend=False)
```

```{code-cell} ipython3
data_type, data_type_name = "hfradar", "HFRadar"
srange = (0, 2.5)
# make_td_by_season(df_hfradar, data_type, data_type_name, srange)
for variable in ["east", "north"]:
    make_td_by_region(df_hfradar_no_nans, data_type, data_type_name, srange, plot_var=variable, extend=False)
```

```{code-cell} ipython3
data_type, data_type_name = "hfradar", "HFRadar"
srange = (0, 2)
# make_td_by_season(df_hfradar, data_type, data_type_name, srange)
for variable in ["east", "north"]:
    make_td_by_region(df_hfradar, data_type, data_type_name, srange, plot_var=variable, extend=False)
```

```{code-cell} ipython3
data_type, data_type_name = "hfradar", "HFRadar"
srange = (0, 2.5)
# make_td_by_season(df_hfradar, data_type, data_type_name, srange)
for variable in ["east", "north"]:
    make_td_by_region(df_hfradar, data_type, data_type_name, srange, plot_var=variable, extend=False)
```

```{code-cell} ipython3

```

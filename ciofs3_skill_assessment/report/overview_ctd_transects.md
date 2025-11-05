---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: ciofs3-report
  language: python
  name: python3
---

# Overview CTD Transects

The performance of the CIOFSv3 model for CTD transect data is summarized on this page. Shown below are a map of dataset locations, Taylor diagrams summarizing performance across the three CIOFS historical models, and overview maps showing markers colored to indicate the skill score of the model-data comparisons for each dataset.

* [165MB zipfile of plots and stats files](https://files.axds.co/ciofs3/zip/ctd_transects.zip)
* [289MB zipfile of CTD profile plots from CTD transects](https://files.axds.co/ciofs3/zip/ctd_profiles_from_transects.zip)
* [180MB CTD transect model-data comparison as PDF](https://files.axds.co/ciofs3/pdfs/ctd_transects.pdf)

```{code-cell} ipython3
:tags: [remove-input]

import intake
import numpy as np
import ocean_model_skill_assessor as omsa
import cook_inlet_catalogs as cic
import pandas as pd
import xarray as xr
import hvplot.pandas
import cmocean
import yaml
from myst_nb import glue
import fnmatch
from datetimerange import DateTimeRange
from holoviews import opts
from bokeh.models import FixedTicker
import holoviews as hv
import os
from pathlib import Path
import subprocess

hv.extension('bokeh')

ins_type = "ctd_transects"  # instrument name
models = ["ciofs3"]

years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 
         2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]


# can only do these when running in docker with playwright available
# once they exist, can run outside of docker because don't need to
# recreate the png files
run_pdf = True
```

```{code-cell} ipython3
:tags: [remove-input]

def save_png(abs_path, figname):
    if not run_pdf:
        # print("Skipping PNG creation because run_pdf is False")
        return
    # Define the command and its arguments
    cmd = [
        "playwright",
        "screenshot",
        f"file://{abs_path}",
        f"{figname}.png",
        # "--full-page",
        "--wait-for-timeout=30000"
    ]

    # Run the command
    if not Path(f"{figname}.png").exists():
        result = subprocess.run(cmd, capture_output=True, text=True)
```

## Map of Stations

```{code-cell} ipython3
:tags: [remove-input]

slugs = [        "ctd_transects_barabara_to_bluff_2002_2003",
        "ctd_transects_cmi_kbnerr", 
        "ctd_transects_cmi_uaf",  
        "ctd_transects_gwa", 
        "ctd_transects_misc_2002",
        "ctd_transects_otf_kbnerr",
        "ctd_transects_uaf",  
        ]

# hand-selected source names to use since often repeated
source_names = {"ctd_transects_barabara_to_bluff_2002_2003": ["Cruise 1"],
                "ctd_transects_cmi_kbnerr": ["Cruise_14-Line_1",
                                             "Cruise_14-Line_2",
                                             "Cruise_14-Line_3",
                                             "Cruise_14-Line_4",
                                             "Cruise_14-Line_6",
                                             "Cruise_14-Line_7",
                                            "sue_shelikof"],
                "ctd_transects_cmi_uaf": ["Cruise-01"],
        "ctd_transects_gwa": ['transect_3-2012-05-02',
                              'transect_4-2012-05-02',
                              'transect_6-2012-05-03',
                              'transect_7-2012-07-30',
                              'transect_9-2012-02-14',
                              'transect_AlongBay-2012-08-15',], 
        "ctd_transects_misc_2002": ['Bear_Jul-02',
                                'Cohen',
                                'Glacier',
                                'Peterson_Jul-02',
                                'PtAdam_jul-02',
                                'pogibshi_Jul-02'],
        "ctd_transects_otf_kbnerr": ['2003-07-01'],
        "ctd_transects_uaf": ['Transect_01'], 
               }
# hand-written names to label with
line_names = {"ctd_transects_barabara_to_bluff_2002_2003": ["Barabara to Bluff (repeated)"],
                "ctd_transects_cmi_kbnerr": ["CMI KBNERR: Line 1 (repeated)",
                                             "CMI KBNERR: Line 2 (repeated)",
                                             "CMI KBNERR: Line 3 (repeated)",
                                             "CMI KBNERR: Line 4 (repeated)",
                                             "CMI KBNERR: Line 6 (repeated)",
                                             "CMI KBNERR: Line 7 (repeated)",
                                            "CMI KBNERR: Sue Shelikof"],
                "ctd_transects_cmi_uaf": ["CMI UAF (repeated)"],
        "ctd_transects_gwa": ['GWA: Transect 3 (repeated)',
                              'GWA: Transect 4 (repeated)',
                              'GWA: Transect 6 (repeated)',
                              'GWA: Transect 7 (repeated)',
                              'GWA: Transect 9 (repeated)',
                              'GWA: Transect AlongBay (repeated)',], 
        "ctd_transects_misc_2002": ['Bear Jul 02',
                                     'Cohen',
                                     'Glacier',
                                     'Peterson Jul 02',
                                     'PtAdam Jul 02',
                                     'Pogibshi Jul 02'],
        "ctd_transects_otf_kbnerr": ['OTF KBNERR (repeated)'],
        "ctd_transects_uaf": ['UAF (repeated)'], 
               }
# hand-written names to label slugs with
slug_names = {"ctd_transects_barabara_to_bluff_2002_2003": "Barabara to Bluff",
                "ctd_transects_cmi_kbnerr": "CMI KBNERR",
                "ctd_transects_cmi_uaf": "CMI UAF",
        "ctd_transects_gwa": "GWA",
        "ctd_transects_misc_2002": "Misc 2002",
        "ctd_transects_otf_kbnerr": "OTF KBNERR",
        "ctd_transects_uaf": "UAF",
               }
```

```{code-cell} ipython3
:tags: [remove-input]

import geopandas as gpd
from shapely.geometry import LineString

rows = []
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    for source_name, label in zip(source_names[slug], line_names[slug]):
        
        dfd = cat[source_name].read().reset_index()
        geometry = LineString(zip(dfd.cf["longitude"].iloc[[0,-1]], dfd.cf["latitude"].iloc[[0,-1]]))
        start_time = cat[source_name].metadata["minTime"]
        rows.append([source_name, geometry, start_time, slug, slug_names[slug], label])
gdf = gpd.GeoDataFrame(rows, columns=["source_name","geometry","date_time", "slug", "slug_labels", "label"])
```

```{code-cell} ipython3
:tags: [remove-input]

figname = f"build_figures/{ins_type}_map"
abs_path = os.path.abspath(f"{figname}.html")

fmap = gdf.hvplot.paths(x="lon", y="lat", geo=True, tiles=True,
                                   #  # xlim=[-153, -150], ylim=[59,60], 
                                    hover_cols=["label"],#,"date_time","slug"],
                                    by="slug_labels", #clabel=station,
                                   legend="top_left", line_width=6, coastline=False, 
                                    xlabel="Longitude", ylabel="Latitude", 
                                    title="CTD Transects", alpha=0.9,
                                    width=600, height=700, fontscale=1.5, )
if not Path(f"{figname}.png").exists():
    hv.save(fmap, figname, fmt='html')
    save_png(abs_path, figname)

glue("fig_map", fmap, display=False)
```

````{div} full-width   
```{glue:figure} fig_map
:name: "fig-overview-ctd-transects-map"

All CTD transects (repeats indicated but not plotted), by project. Click on a legend entry to toggle the transparency.

```
````

+++

````{div} full-width                
```{figure} build_figures/ctd_transects_map.png
:name: "fig-overview-ctd-transects-map"

All CTD transects, by project.
```
````

+++

## Taylor Diagrams

The present Taylor diagrams summarize the skill of the three historical CIOFS models in capturing the CTD transect datasets. Only datasets from years for which all three CIOFS historical models are available are used, which are 2003-2006 and 2012-2014 (the years modeled for CIOFS fresh).

The data has been grouped by region ({numref}`Fig. {number}<fig-ctd_transects_by_region>`) and season ({numref}`Fig. {number}<fig-ctd_transects_by_season>`). For temperature, the models behave similarly to each other and perform well across regions (correlation coefficient $r$ ranges from 0.8 to 0.99 and have accurate variance). There is more separation in performance by season with CIOFS Fresh and CIOFSv3 outperforming CIOFS Hindcast. Fall shows the least accuracy ($r\sim0.7$ for CIOFSv3) and summer shows the best ($r\sim0.95$). As expected for salinity, CIOFS Hindcast performs poorly; CIOFSv3 performs better than CIOFS Fresh across regions except has too much variance in Kachemak Bay (and the two are similar in lower Cook Inlet). Correlation coefficients for CIOFSv3 range from ~0.5 in Kachemak Bay to ~0.95 in central Cook Inlet, and variance alternates between too low (outside and lower Cook Inlet) and too high (central and upper Cook Inlet and Kachemak Bay). By season, CIOFS Fresh and CIOFSv3 perform similarly and does pretty well ($r\sim0.8$ to $r\sim0.95$ with too high variance in all seasons except winter).


```{figure} ../figures/taylor_diagrams/ctd_transects_by_region.png
---
name: fig-ctd_transects_by_region
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for temperature (left) and salinity (right), grouped by region of Cook Inlet, for CTD transects datasets.
```


```{figure} ../figures/taylor_diagrams/ctd_transects_by_season.png
---
name: fig-ctd_transects_by_season
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for temperature (left) and salinity (right), grouped by season, for CTD transects datasets.
```

```{code-cell} ipython3
:tags: [remove-input]

# hand-written globs to select transects
line_globs = {"ctd_transects_barabara_to_bluff_2002_2003": ["*"],
                "ctd_transects_cmi_kbnerr": ["*Line_1*",
                                             "*Line_2*",
                                             "*Line_3*",
                                             "*Line_4*",
                                             "*Line_6*",
                                             "*Line_7*",
                                            "*sue_shelikof*"],
                "ctd_transects_cmi_uaf": ["*"],
        "ctd_transects_gwa": ['*transect_3*',
                              '*transect_4*',
                              '*transect_6*',
                              '*transect_7*',
                              '*transect_9*',
                              '*transect_AlongBay*',], 
        "ctd_transects_misc_2002": ['*Bear_Jul-02*',
                                     '*Cohen*',
                                     '*Glacier*',
                                     '*Peterson_Jul-02*',
                                     '*PtAdam_jul-02*',
                                     '*pogibshi_Jul-02*'],
        "ctd_transects_otf_kbnerr": ['*'],
        "ctd_transects_uaf": ['*'], 
               }
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, model_name, key_variable, glob_source_names):
    # ctd_transects_barabara_to_bluff_2002_2003_Cruise 10_temp.yaml
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = []
    # import pdb; pdb.set_trace()
    for source_name in glob_source_names:
        stats_fnames.extend(list(paths.OUT_DIR.glob(f"*{source_name.replace(' ', '_')}_{key_variable}.yaml")))
    return sorted(stats_fnames)

def load_ss(index, stats_fnames, model_name, key_variable):
    ds = pd.Series(index=index, dtype=float)
    for stats_fname in stats_fnames:
        with open(stats_fname, "r") as stream:
            stats = yaml.safe_load(stream)
            ss = stats["ss"]["value"]
            mse = stats["mse"]["value"]
            if ss == 1.0 and np.isnan(mse):
                ss = np.nan
            station = stats_fname.name.split(slug)[1].split(key_variable)[0].strip("_")
            ds.loc[station] = ss
    return ds
```

```{code-cell} ipython3
:tags: [remove-input]

def station_intersect_with_years(minTime, maxTime):
    # if there is any overlap between data and years, include
    data_time_range = DateTimeRange(minTime, maxTime)
    flag = False
    for year in years:
        start = pd.Timestamp(f"{year}-01-01")
        end = pd.Timestamp(f"{year}-12-31")
        model_time_range = DateTimeRange(start, end)
        flag += data_time_range.is_intersection(model_time_range)
    return flag
```

```{code-cell} ipython3
:tags: [remove-input]

# go through every cat
# read stats files for all sources by transect
# input them into temp dataframe tracking that
# get end points lon/lat from original df and calculate mid points, append to list, combine at the end

model_names, key_variables = models, ["temp", "salt"]
vardescs = ["sea temperature", "salinity"]
mindex = pd.MultiIndex.from_product([model_names, key_variables])

# slugs = [       
#     "ctd_transects_barabara_to_bluff_2002_2003",
#         "ctd_transects_cmi_kbnerr", 
#         "ctd_transects_cmi_uaf",  
#         "ctd_transects_gwa", 
#         "ctd_transects_otf_kbnerr",
#         "ctd_transects_uaf",  
#         ]

dfs = {}
for model_name in model_names:
    for key_variable in key_variables:
        dfouts = []
        all_source_names, all_slugs, all_times, all_slug_labels = [], [], [], []
        all_lons, all_lats = [], []
        for slug in slugs:
            cat = intake.open_catalog(cic.utils.cat_path(slug))
            source_names = list(cat)
            skip_source_names = []
            # check which source_names from catalog are in time frame
            for source_name in source_names:
                minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
                if not station_intersect_with_years(minTime, maxTime):
                    # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
                    skip_source_names.append(source_name)
                    continue

            for lglob in line_globs[slug]:
                
                # import pdb; pdb.set_trace()
                glob_source_names = fnmatch.filter(source_names,lglob)  # these are the source names for this part of dataframe
                # skip_source_names
                glob_source_names = sorted(list(set(glob_source_names) - set(skip_source_names)))
                all_source_names.extend(glob_source_names)
                all_slugs.extend([slug]*len(glob_source_names))
                all_slug_labels.extend([slug_names[slug]]*len(glob_source_names))
                all_times.extend([cat[source_name].metadata["minTime"][:13] for source_name in glob_source_names])
                stats_fnames = return_paths(slug, model_name, key_variable, glob_source_names)
                # stats_fnames = return_paths(slug, model_name, key_variable, lglob)
                # import pdb; pdb.set_trace()
                glob_source_names = [source_name.replace(" ", "_") for source_name in glob_source_names]
                dfouttemp = load_ss(glob_source_names, stats_fnames, model_name, key_variable)
                
                whichrows = fnmatch.filter(gdf[gdf["slug"] == slug]["source_name"],lglob)
                # import pdb; pdb.set_trace()
                lon_endpoints, lat_endpoints = list(zip(*(gdf[gdf["source_name"].isin(whichrows)]["geometry"].values[0].coords)))
                # lon_endpoints = gdf[gdf["source_name"].isin(whichrows)]["lon"].dropna().to_list()
                # lat_endpoints = gdf[gdf["source_name"].isin(whichrows)]["lat"].dropna().to_list()
                lons = np.linspace(*lon_endpoints, len(glob_source_names))
                lats = np.linspace(*lat_endpoints, len(glob_source_names))

                if slug == "ctd_transects_cmi_kbnerr":
                    lats += 0.03
                elif slug == "ctd_transects_gwa":
                    lats -= 0.025
                elif slug == "ctd_transects_otf_kbnerr":
                    lats -= 0.04

                all_lons.extend(lons)
                all_lats.extend(lats)
                dfouts.append(dfouttemp)
        dfout = pd.concat(dfouts, axis=0)
        dfs[f"{model_name}_{key_variable}"] = dfout
    
data = pd.concat(dfs, axis=1).values
dfall = pd.DataFrame(data, index=all_source_names, columns=mindex)
dfall.index.name = "source_name"
dfall.index = dfall.index.astype("string")  # ensure index is string type
dfall["lon"] = all_lons
dfall["lat"] = all_lats
dfall["date_time"] = pd.to_datetime(all_times)
dfall["slug"] = all_slugs
dfall["slug_label"] = all_slug_labels
dfall["slug_label"] = dfall["slug_label"].astype("category")
dfall = dfall.reset_index().set_index(["source_name","lon","lat","date_time","slug", "slug_label"])
```

```{code-cell} ipython3
:tags: [remove-input]

newcmap = cmocean.cm.matter

hovers = [("Slug", "@slug_label"),
          ("Station", "@source_name"),
          ("Time", "@date_time"),
          ("Longitude", "@lon"),
          ("Latitude", "@lat"),
          ("SS bin", "@ss_range"),
          ]
hover_cols = ["slug_label", "source_name", "date_time", "lon", "lat", "ss_range"]

# inputs = dict(x="lon", y="lat", c="ss", hover=False)# hover_cols=hover_cols)
inputs = dict(x="lon", y="lat", c="ss_code", hover_cols=hover_cols)

plot_kwargs = dict(geo=True, tiles=True, size=50, width=600, height=700, clim=(0,1), cmap=newcmap,
                #   coastline="10m", 
                  xlabel="Longitude", ylabel="Latitude", by="slug_label", legend="top_left",
                  fontscale=1.5, marker='s')


# setup for changing colorbar from continuous to categorical
# which saves SO MUCH MEMORY
nbins = 11
cat_bins = np.linspace(0,1,nbins)
ticks = list(range(0,nbins))
tick_labels = {i: f"{i/(nbins-1):.1f}" for i in ticks}


opts_pts = hv.opts.Points(
    color_levels=10,
    clim=(0,10),
    colorbar_opts={'ticker': FixedTicker(ticks=ticks), 'major_label_overrides': tick_labels},
    tools=["hover"], hover_tooltips=hovers
    )
```

```{code-cell} ipython3
:tags: [remove-input]

def plot(model_name, key_variable, vardesc):
    clabel = f"{model_name.upper()} model skill scores for CTD transects for {vardesc}"
    # dfallsub = dfall.loc[:,(model_names,key_variable)]
    dfallsubsub = dfall.loc[:,(model_name,key_variable)].dropna().rename("ss")
    cats = pd.cut(dfallsubsub, cat_bins).to_frame()
    cats["ss_code"] = cats["ss"].cat.codes
    cats["ss_range"] = cats["ss"].astype(str)

    # we plot the category codes but then label the colorbar correctly
    # so we don't have to plot a continuous colorbar with many levels
    return cats.hvplot.points(**inputs, **plot_kwargs, title=vardesc.capitalize(), clabel=clabel).opts(opts_pts)
```

```{code-cell} ipython3
:tags: [remove-input]

def make_figures(model, key_variables, vardescs):
    
    figname = f"build_figures/{ins_type}"
    abs_path = os.path.abspath(f"{figname}.html")

    plots = []
    for key_variable, vardesc in zip(key_variables, vardescs):
        plots.append(plot(model, key_variable, vardesc))

    variable_plot = plots[0] + plots[1]

    if not Path(f"{figname}.png").exists():
        hv.save(variable_plot, figname, fmt='html')
        if run_pdf:
            save_png(abs_path, figname)

    return variable_plot, figname, abs_path
```

## Skill Scores

Each colored square marker represents the skill score for the model compared with the data for a visit to the transect. The length of each transect was split into the number of visits with a square for each visit; if there were many repeat visits there are a lot of squares along a transect and only one for a single visit.

Results show good skill for both temperature and salinity, though occasional transects have low skill.

```{code-cell} ipython3
:tags: [remove-input]

ctd_transects, figname, abs_path = make_figures(models[0], key_variables, vardescs)
glue("ctd_transects", ctd_transects, display=False)
```

````{div} full-width   
```{glue:figure} ctd_transects
:name: "fig-overview-ctd-transects"

Skill scores for CIOFSv3 with CTD transects for sea temperature (left) and salinity (right), by project. Click on a legend entry to toggle the transparency.
```
````

+++

```{figure} build_figures/ctd_transects.png
:name: "fig-overview-ctd-transects"

Skill scores for CIOFSv3 with CTD transects for sea temperature (left) and salinity (right), by project.
```

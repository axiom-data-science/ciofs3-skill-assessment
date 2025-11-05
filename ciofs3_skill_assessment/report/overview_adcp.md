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

(page:overview_adcp)=
# Overview ADCP Data

The performance of the CIOFSv3 model for ADCP data is summarized on this page. Shown below are a map of dataset locations, Taylor diagrams summarizing performance across the three CIOFS historical models, and overview maps showing markers colored to indicate the skill score of the model-data comparisons for each dataset.

* [60MB zipfile of plots and stats files](https://files.axds.co/ciofs3/zip/adcp.zip)
* [70MB ADCP model-data comparison as PDF](https://files.axds.co/ciofs3/pdfs/adcp.pdf)

```{code-cell} ipython3
:tags: [remove-input]

import intake
import numpy as np
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import matplotlib.pyplot as plt
    import ocean_model_skill_assessor as omsa
import cook_inlet_catalogs as cic
import pandas as pd
import xarray as xr
import hvplot.pandas
import cmocean
import yaml
from myst_nb import glue
from datetimerange import DateTimeRange
from holoviews import opts
from bokeh.models import FixedTicker
import holoviews as hv
import os
from pathlib import Path
import subprocess


ins_type = "adcp"  # instrument name
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

slugs = ["adcp_moored_noaa_coi_2005",
        "adcp_moored_noaa_coi_other",
        'adcp_moored_noaa_kod_1',
        'adcp_moored_noaa_kod_2',
        ]
slug_names = {
    "adcp_moored_noaa_coi_2005": "NOAA Cook Inlet 2005",
    "adcp_moored_noaa_coi_other": "NOAA Cook Inlet Other",
    'adcp_moored_noaa_kod_1': "NOAA Kodiak 1",
    'adcp_moored_noaa_kod_2': "NOAA Kodiak 2",
}
rows = []
source_names_present = {}
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = [sn for sn in list(cat) if sn not in ["COI0301","COI0303"]]
    source_names_present[slug] = []
    for source_name in source_names:
        lon, lat = cat[source_name].metadata["minLongitude"], cat[source_name].metadata["minLatitude"]
        start_time = cat[source_name].metadata["minTime"]
        minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
        if not station_intersect_with_years(minTime, maxTime):
            # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
            continue
        # print(f"Adding {source_name} because min time {minTime} and max time {maxTime} are in {years}")
        source_names_present[slug].append(source_name)
        rows.append([source_name, lon, lat, start_time, slug, slug_names[slug]])
df = pd.DataFrame(rows, columns=["station","lon","lat","start_time", "slug", "slug_name"])
```

```{code-cell} ipython3
:tags: [remove-input]

figname = f"build_figures/{ins_type}_map"
abs_path = os.path.abspath(f"{figname}.html")

fmap = df.hvplot.points(x="lon", y="lat", by="slug_name",
                legend="top_left", geo=True, tiles=True, size=50, hover_cols=["station","start_time"],
                xlabel="Longitude", ylabel="Latitude", title="ADCP Moorings",
                width=600, height=700, marker="o", fontscale=1.5,)# coastline="10m")
if not Path(f"{figname}.png").exists():
    hv.save(fmap, figname, fmt='html')
    save_png(abs_path, figname)
glue("fig_map", fmap, display=False)
```

````{div} full-width   
```{glue:figure} fig_map
:name: "fig-overview-adcp-map"

All ADCP deployments, by project. Click on a legend entry to toggle the transparency.
```
````

+++

````{div} full-width                
```{figure} build_figures/adcp_map.png
:name: "fig-overview-adcp-map"

All ADCP deployments, by project.
```
````

+++

## Taylor Diagrams

The present Taylor diagrams summarize the skill of the three historical CIOFS models in capturing the ADCP datasets. Only datasets from years for which all three CIOFS historical models are available are used, which are 2003-2006 and 2012-2014 (the years modeled for CIOFS fresh).

The data has been grouped by region (Figs. {numref}`{number}<fig-adcp_moored_by_region_east>`, {numref}`{number}<fig-adcp_moored_by_region_north>`, {numref}`{number}<fig-adcp_moored_by_region_speed>`) and season (Figs. {numref}`{number}<fig-adcp_moored_by_season_east>`, {numref}`{number}<fig-adcp_moored_by_season_north>`, {numref}`{number}<fig-adcp_moored_by_season_speed>`). The results show that the models perform similarly for tidal results. 

The variance for CIOFS Fresh and CIOFSv3 is mostly accurate for the subtidal along-channel velocity component, across regions, whereas CIOFS Hindcast is mostly low. Correlation is similar for the models and is lowest ($r\sim0.3$) outside Cook Inlet and highest ($r\sim0.9$) in central Cook Inlet. Subtidal along-channel velocity is more accurately predicted in the spring ($r\sim0.9$ correlation) than the summer ($r\sim0.7$ correlation). Subtidal across-channel velocity comparisons are more scattered. Correlation coefficients are between 0.4 and 0.7 across regions but with widely varying variance and relative model performance. Subtidal across-channel velocity is predicted more accurately in the summer ($r\sim0.6$) than the spring ($r\sim0.4$). The subtidal speed is mostly well-captured across regions by the models with correlation coefficients between 0.8 (upper Cook Inlet) and 0.99 (Kachemak Bay) and similar variance to the data, with models performing similarly. By season, the models are clustered with accurate variance and correlation of 0.95.

```{figure} ../figures/taylor_diagrams/adcp_moored_by_region_east.png
---
name: fig-adcp_moored_by_region_east
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for the along-channel component of velocity with tides (left) and subtidal (right), grouped by region of Cook Inlet, for moored ADCP datasets.
```

```{figure} ../figures/taylor_diagrams/adcp_moored_by_region_north.png
---
name: fig-adcp_moored_by_region_north
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for the across-channel component of velocity with tides (left) and subtidal (right), grouped by region of Cook Inlet, for moored ADCP datasets.
```

```{figure} ../figures/taylor_diagrams/adcp_moored_by_region_speed.png
---
name: fig-adcp_moored_by_region_speed
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for the magnitude of velocity with tides (left) and subtidal (right), grouped by region of Cook Inlet, for moored ADCP datasets.
```

```{figure} ../figures/taylor_diagrams/adcp_moored_by_season_east.png
---
name: fig-adcp_moored_by_season_east
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for the along-channel component of velocity with tides (left) and subtidal (right), grouped by season, for moored ADCP datasets.
```

```{figure} ../figures/taylor_diagrams/adcp_moored_by_season_north.png
---
name: fig-adcp_moored_by_season_north
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for the across-channel component of velocity with tides (left) and subtidal (right), grouped by season, for moored ADCP datasets.
```

```{figure} ../figures/taylor_diagrams/adcp_moored_by_season_speed.png
---
name: fig-adcp_moored_by_season_speed
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for the magnitude of velocity with tides (left) and subtidal (right), grouped by season, for moored ADCP datasets.
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, model_name, key_variable, which, stations_this_slug):
    paths = omsa.Paths(f"{slug}_{model_name}")
    # import pdb; pdb.set_trace()
    
    if which == "tidal":
        which_str = ""
    elif which == "subtidal":
        which_str = "_subtidal"

    stats_fnames = []
    for station in stations_this_slug:
        stats_fnames.extend(sorted(paths.OUT_DIR.glob(f"{slug}_{station}_{key_variable}{which_str}.yaml")))

    # if which == "tidal":
    #     stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}.yaml"))
    # elif which == "subtidal":
    #     stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}_{which}.yaml"))
    # if slug == "adcp_moored_noaa_coi_other":
    #     import pdb; pdb.set_trace()
    stats_fnames = [name for name in stats_fnames if "COI0301" not in str(name) and "COI0303" not in str(name)]
    return stats_fnames

def load_ss(index, stats_fnames, model_name, key_variable):
    # print(len(index), len(stats_fnames))
    ds = pd.Series(index=index, dtype=float)
    for stats_fname in stats_fnames:
        with open(stats_fname, "r") as stream:
            stats = yaml.safe_load(stream)
            ss = stats["ss"]["value"]
            mse = stats["mse"]["value"]
            if ss == 1.0 and np.isnan(mse):
                # import pdb; pdb.set_trace()
                ss = np.nan
            station = stats_fname.name.split(slug)[1].split(key_variable)[0].strip("_")
            ds.loc[station] = ss
    return ds
```

```{code-cell} ipython3
:tags: [remove-input]

model_names, key_variables, whichs = models, ["speed_rotate","east_rotate","north_rotate"], ["tidal","subtidal"]
# vardescs = ["Speed", "Along-Channel Velocity", "Across-Channel Velocity"]
vardescs = {"speed_rotate": "Speed", "east_rotate": "Along-Channel Velocity", "north_rotate": "Across-Channel Velocity"}
dfalls = []
for slug in slugs:
    dfs = {}
    stations_this_slug = df[df["slug"] == slug]["station"]
    for model_name in model_names:
        for key_variable in key_variables:
            for which in whichs:
                stats_fnames = return_paths(slug, model_name, key_variable, which, stations_this_slug)
                # if len(stations_this_slug) != len(stats_fnames):
                #     import pdb; pdb.set_trace()
                dfout = load_ss(stations_this_slug, stats_fnames, model_name, key_variable)
                dfs[f"{model_name}_{key_variable}_{which}"] = dfout
    mindex = pd.MultiIndex.from_product([model_names, key_variables, whichs])
    data = pd.concat(dfs, axis=1).values
    # print(model_name, slug)
    # if slug == "adcp_moored_noaa_coi_other":
    #     import pdb; pdb.set_trace()
    dfalltemp = pd.DataFrame(data, index=stations_this_slug, columns=mindex)
    dfalls.append(dfalltemp)
dfall = pd.concat(dfalls, axis=0)
inds = ["lon","lat","start_time","slug", "slug_name"]
dfall[inds] = df.set_index("station")[inds]
dfall = dfall.reset_index().set_index(["station",*inds])
```

```{code-cell} ipython3
:tags: [remove-input]

newcmap = cmocean.cm.matter

hovers = [("Slug", "@slug_name"),
          ("Station", "@station"),
          ("Start Time", "@start_time"),
          ("Longitude", "@lon"),
          ("Latitude", "@lat"),
          ("SS bin", "@ss_range"),
          ]
hover_cols = ["slug_name", "station", "start_time", "lon", "lat", "ss_range"]


# inputs = dict(x="lon", y="lat", c="ss", by="slug_name", hover=False)
inputs = dict(x="lon", y="lat", c="ss_code", hover_cols=hover_cols, by="slug_name")
plot_kwargs = dict(geo=True, tiles=True, size=100, width=600, height=700, clim=(0,1), cmap=newcmap,
                #   coastline="10m", 
                  xlabel="Longitude", ylabel="Latitude", legend="top_left",
                  fontscale=1.5)


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

def plot(dfall, model_name, key_variable, which):
    clabel = f"{model_name.upper()} skill scores (ADCP moorings): {which} {vardescs[key_variable].lower()}"
    dfallsub = dfall.loc[:,(model_names,key_variable,which)]
    dfallsubsub = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss")
    cats = pd.cut(dfallsubsub, cat_bins).to_frame()
    cats["ss_code"] = cats["ss"].cat.codes
    cats["ss_range"] = cats["ss"].astype(str)

    # we plot the category codes but then label the colorbar correctly
    # so we don't have to plot a continuous colorbar with many levels
    return cats.hvplot.points(**inputs, **plot_kwargs, title=f"{which.capitalize()} {vardescs[key_variable]}", clabel=clabel).opts(opts_pts)
```

```{code-cell} ipython3
:tags: [remove-input]

def make_figures(model, key_variable, which):


    if len(key_variable) == 2:
        figname = f"build_figures/{ins_type}_{which}_{key_variable[0]}_{key_variable[1]}"
        plots = []
        for key_var in key_variable:
            plots.append(plot(dfall, model, key_var, which))

        variable_plot = plots[0] + plots[1]
    else:
        figname = f"build_figures/{ins_type}_{which}_{key_variable}"
        variable_plot = plot(dfall, model, key_variable, which)

    abs_path = os.path.abspath(f"{figname}.html")

    if not Path(f"{figname}.png").exists():
        hv.save(variable_plot, figname, fmt='html')
        save_png(abs_path, figname)

    return variable_plot, figname, abs_path
```

## Skill Scores

The CIOFSv3 model has high skill in representing the tidal speed and along- and across-channel velocities through the main Cook Inlet channel. Outside of the Inlet, around Kodiak Island, skill scores drop from over 0.9 to 0.3 to 0.6 for tidal speed and along-channel velocity and mostly low skill for across-channel velocity. Skill scores for subtidal speed are similar to tidal speed: high in the Inlet and lower outside. Subtidal velocity component skill scores are mostly over 0.5 in the Inlet and under 0.5 around Kodiak Island.


### Tidal

+++

#### Horizontal Speed

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "speed_rotate", "tidal"

tidal_speed, figname, abs_path = make_figures(models[0], key_variable, which)
glue("tidal_speed", tidal_speed, display=False)
```

````{div} full-width   
```{glue:figure} tidal_speed
:name: "fig-overview-adcp-tidal-speed"

Skill scores for CIOFSv3 with ADCP moorings for horizontal speed, by project. Click on a legend entry to toggle the transparency.
```
````

+++

```{figure} build_figures/adcp_tidal_speed_rotate.png
:name: "fig-overview-adcp-tidal-speed"

Skill scores for CIOFSv3 with ADCP moorings for horizontal speed, by project.
```

+++

#### Along- and Across-Channel Velocity

```{code-cell} ipython3
:tags: [remove-input]

key_variables, which = ["east_rotate", "north_rotate"], "tidal"

both_tidal, figname, abs_path = make_figures(models[0], key_variables, which)
glue("both_tidal", both_tidal, display=False)
```

````{div} full-width   
```{glue:figure} both_tidal
:name: "fig-overview-adcp-tidal"

Skill scores for CIOFSv3 with ADCP moorings for along-channel (left) and across-channel velocity (right), by project. Click on a legend entry to toggle the transparency.
```
````

+++

```{figure} build_figures/adcp_tidal_east_rotate_north_rotate.png
:name: "fig-overview-adcp-tidal"

Skill scores for CIOFSv3 with ADCP moorings for along-channel (left) and across-channel velocity (right), by project.
```

+++

### Subtidal

+++

#### Horizontal Speed

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "speed_rotate", "subtidal"

subtidal_speed, figname, abs_path = make_figures(models[0], key_variable, which)
glue("subtidal_speed", subtidal_speed, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_speed
:name: "fig-overview-adcp-subtidal-speed"

Skill scores for CIOFSv3 with ADCP moorings for subtidal horizontal speed, by project. Click on a legend entry to toggle the transparency.
```
````

+++

```{figure} build_figures/adcp_subtidal_speed_rotate.png
:name: "fig-overview-adcp-subtidal-speed"

Skill scores for CIOFSv3 with ADCP moorings for subtidal horizontal speed, by project.
```

+++

#### Along- and Across-Channel Velocity

```{code-cell} ipython3
:tags: [remove-input]

key_variables, which = ["east_rotate", "north_rotate"], "subtidal"

both_subtidal, figname, abs_path = make_figures(models[0], key_variables, which)
glue("both_subtidal", both_subtidal, display=False)
```

````{div} full-width   
```{glue:figure} both_subtidal
:name: "fig-overview-adcp-subtidal"

Skill scores for CIOFSv3 with ADCP moorings for subtidal along-channel (left) and across-channel velocity (right), by project. Click on a legend entry to toggle the transparency.
```
````

+++

```{figure} build_figures/adcp_subtidal_east_rotate_north_rotate.png
:name: "fig-overview-adcp-subtidal"

Skill scores for CIOFSv3 with ADCP moorings for subtidal along-channel (left) and across-channel velocity (right), by project.
```

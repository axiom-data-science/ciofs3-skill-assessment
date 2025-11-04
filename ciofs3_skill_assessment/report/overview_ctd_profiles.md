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

# Overview CTD Profiles

The performance of the CIOFSv3 model for CTD profiles data is summarized on this page. Shown below are a map of dataset locations, Taylor diagrams summarizing performance across the three CIOFS historical models, and overview maps showing markers colored to indicate the skill score of the model-data comparisons for each dataset.

* [60MB zipfile of plots and stats files](https://files.axds.co/ciofs3/zip/ctd_profiles.zip)
* [55MB CTD profile model-data comparison as PDF](https://files.axds.co/ciofs3/pdfs/ctd_profiles.pdf)

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

ins_type = "ctd_profiles"  # instrument name
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

lonmin, lonmax, latmin, latmax = -156.485291, -148.925125, 56.7004919, 61.5247774

def stations_inside_domain(lon, lat):
    # compare if the drifter is even in the domain box
    if lonmin <= lon <= lonmax and latmin <= lat <= latmax:
        return True
    else:
        return False
```

```{code-cell} ipython3
:tags: [remove-input, remove-output]

slugs = ['ctd_profiles_2005_noaa',
 'ctd_profiles_ecofoci',
 'ctd_profiles_emap_2002',
 'ctd_profiles_emap_2008',
 'ctd_profiles_kachemack_kuletz_2005_2007',
 'ctd_profiles_kb_small_mesh_2006',
 'ctd_profiles_kbay_osu_2007',
 'ctd_profiles_piatt_speckman_1999',
 'ctd_profiles_usgs_boem',
 ]
slug_names = {
    "ctd_profiles_2005_noaa": "NOAA 2005",
    "ctd_profiles_kachemack_kuletz_2005_2007": "K. Kuletz 2005-2007",
    "ctd_profiles_kb_small_mesh_2006": "K. Bay Small Mesh 2006",
    "ctd_profiles_kbay_osu_2007": "K. Bay OSU 2007",
    "ctd_profiles_piatt_speckman_1999": "Piatt Speckman 1999",
    "ctd_profiles_ecofoci": "EcoFOCI",
    "ctd_profiles_emap_2002": "EMAP 2002",
    "ctd_profiles_emap_2008": "EMAP 2008",
    "ctd_profiles_usgs_boem": "USGS BOEM",
}
rows = []
source_names_present = {}
for slug in slugs:
    # print(slug)
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names_present[slug] = []
    # these stations are generally in the domain but probably right at the coast so a good grid cell isn't being found to match
    source_names = [sn for sn in list(cat) if sn not in ["AKCI08-026","AKCI08-076", "10", "63", "64", "67", "68"]]
    for source_name in source_names:
        lon, lat = cat[source_name].metadata["minLongitude"], cat[source_name].metadata["minLatitude"]
        start_time = cat[source_name].metadata["minTime"]
        minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
        if not station_intersect_with_years(minTime, maxTime):
            # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
            continue
        # print(f"Adding {source_name} because min time {minTime} and max time {maxTime} are in {years}")
        if not stations_inside_domain(lon, lat):
            # print(f"Skipping {source_name} because lon {lon} and lat {lat} are outside domain")
            continue
        source_names_present[slug].append(source_name)
        rows.append([source_name, lon, lat, pd.Timestamp(start_time), slug, slug_names[slug]])
df = pd.DataFrame(rows, columns=["station","lon","lat","date_time", "slug", "slug_names"])
df["slug_names"] = df["slug_names"].astype("category")
```

```{code-cell} ipython3
:tags: [remove-input]

figname = f"build_figures/{ins_type}_map"
abs_path = os.path.abspath(f"{figname}.html")

fmap = df.hvplot.points(x="lon", y="lat", by="slug_names",
                legend="top_left", geo=True, tiles=True, size=40, hover_cols=["station","date_time"],
                coastline=False, xlabel="Longitude", ylabel="Latitude", title="CTD Profiles",
                width=600, height=700, marker="o", alpha=0.75, fontscale=1.25)
if not Path(f"{figname}.png").exists():
    hv.save(fmap, figname, fmt='html')
    if run_pdf:
        save_png(abs_path, figname)

glue("fig_map", fmap, display=False)
```



+++

````{div} full-width                
```{figure} build_figures/ctd_profiles_map.png
:name: "fig-overview-ctd-profiles-map"

All CTD profiles, by project.
```
````

+++

## Taylor Diagrams

The present Taylor diagrams summarize the skill of the three historical CIOFS models in capturing the CTD profile datasets. Only datasets from years for which all three CIOFS historical models are available are used, which are 2003-2006 and 2012-2014 (the years modeled for CIOFS fresh).

The data has been grouped by region ({numref}`Fig. {number}<fig-ctd_profiles_by_region>`) and season ({numref}`Fig. {number}<fig-ctd_profiles_by_season>`). For temperature, the models perform similarly. By region, the lowest performance is in upper Cook Inlet ($r\sim0.2$ and low variance, though CIOFS Hindcast performs anomalously high). Performance is reasonable across the other regions ($r$ between 0.7 and 0.9), but variance is best in Kachemak Bay and outside Cook Inlet. Correlations by season range from 0.4 to 0.9 but variance is much too low in the fall. CIOFS Hindcast performs poorly for salinity comparisons, but does best in the winter and outside Cook Inlet. CIOFS Fresh and CIOFSv3 have too much variance in Kachemak Bay and upper and central Cook Inlet but otherwise have decent correlations ($r>0.8$). CIOFS Fresh and CIOFSv3 perform best in the summer ($r\sim0.95$ and good variance) but are also decent in other seasons (especially CIOFSv3).


```{figure} ../figures/taylor_diagrams/ctd_profiles_by_region.png
---
name: fig-ctd_profiles_by_region
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for temperature (left) and salinity (right), grouped by region of Cook Inlet, for CTD profiles datasets.
```


```{figure} ../figures/taylor_diagrams/ctd_profiles_by_season.png
---
name: fig-ctd_profiles_by_season
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for temperature (left) and salinity (right), grouped by season, for CTD profiles datasets.
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, model_name, key_variable, stations_this_slug):
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = sorted(paths.OUT_DIR / f"{slug}_{station.replace('.', '_')}_{key_variable}.yaml" for station in stations_this_slug)
    # stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}.yaml"))
    # station_intersect_with_years
    # stats_fnames = [name for name in stats_fnames if "AKCI08-026" not in str(name) and "AKCI08-076" not in str(name)]
    # stats_fnames = [name for name in stats_fnames if ("10" not in str(name) and slug == "ctd_profiles_emap_2002")]
    # testnames = [name for name in stats_fnames if "10" in str(name) and slug == "ctd_profiles_emap_2002"]
    # if len(testnames) > 0:
    #     import pdb; pdb.set_trace()
    return stats_fnames

def load_ss(index, stats_fnames, key_variable):
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

model_names, key_variables = models, ["temp", "salt"]
vardescs = ["sea temperature", "salinity"]

dfalls = []
for slug in slugs:
    dfs = {}
    stations_this_slug = df[df["slug"] == slug]["station"]
    for model_name in model_names:
        for key_variable in key_variables:
            stats_fnames = return_paths(slug, model_name, key_variable, stations_this_slug)
            dfout = load_ss(stations_this_slug.str.replace(".","_"), stats_fnames, key_variable)
            dfs[f"{model_name}_{key_variable}"] = dfout
            # print(len(stations_this_slug), len(dfout), model_name, key_variable, slug)
    mindex = pd.MultiIndex.from_product([model_names, key_variables])
    data = pd.concat(dfs, axis=1).values
    dfalltemp = pd.DataFrame(data, index=stations_this_slug, columns=mindex)
    dfalls.append(dfalltemp)
dfall = pd.concat(dfalls, axis=0)
inds = ["lon", "lat", "date_time", "slug", "slug_names"]
dfall[inds] = df.set_index("station")[inds]
dfall = dfall.reset_index().set_index(["station", *inds])
```

```{code-cell} ipython3
:tags: [remove-input]

newcmap = cmocean.cm.matter

hovers = [("Slug", "@slug_names"),
          ("Station", "@station"),
          ("Time", "@date_time"),
          ("Longitude", "@lon"),
          ("Latitude", "@lat"),
          ("SS bin", "@ss_range"),
          ]
hover_cols = ["slug_names", "station", "date_time", "lon", "lat", "ss_range"]

# inputs = dict(x="lon", y="lat", c="ss", hover=False, by="slug_names",)
inputs = dict(x="lon", y="lat", c="ss_code", hover_cols=hover_cols, by="slug_names",)
plot_kwargs = dict(geo=True, tiles=True, size=100, width=600, height=700, clim=(0,1), cmap=newcmap,
                #   coastline="10m", 
                  xlabel="Longitude", ylabel="Latitude", legend="top_left",
                  fontscale=1.25)

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
    clabel = f"{model_name.upper()} model skill scores for CTD profiles for {vardesc}"
    # dfallsub = dfall.loc[:,(model_names,key_variable)]
    # import pdb; pdb.set_trace()
    dfallsubsub = dfall.loc[:,(model_name,key_variable)].dropna().rename("ss")
    cats = pd.cut(dfallsubsub, cat_bins).to_frame()
    cats["ss_code"] = cats["ss"].cat.codes
    cats["ss_range"] = cats["ss"].astype(str)

    # we plot the category codes but then label the colorbar correctly
    # so we don't have to plot a continuous colorbar with many levels
    # import pdb; pdb.set_trace()
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

Model performance is mixed for both temperature and salinity for CTD profiles with both high and low performance present.

```{code-cell} ipython3
:tags: [remove-input]

ctd, figname, abs_path = make_figures(models[0], key_variables, vardescs)
glue("ctd", ctd, display=False)
```



+++

```{figure} build_figures/ctd_profiles.png
:name: "fig-overview-ctd-profiles"

Skill scores for CIOFSv3 with CTD profiles for sea temperature (left) and salinity (right), by project.
```

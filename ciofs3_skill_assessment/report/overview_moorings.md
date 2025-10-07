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

# Overview Mooring Data

UPDATE
In the map below, some stations are at the same or nearly same location, in which case the marker representing their location is shifted slightly to allow for both to be seen. Datasets that span more than 1 year are represented by the number of years they span: one marker per year. By necessity these markers are moved in space from the actual station location and arranged into a grid so they can all be seen. Therefore, their locations in the skill score plots do not represent their actual locations.

The skill scores below represent the skill of each model by variable and processing listed. The models perform similarly for sea surface height: they capture the tidal signal well and the subtidal signal less well, though some improvement is noticeable for CIOFS fresh as compared with CIOFS hindcast for the subtidal sea surface height. The models perform similarly for temperature; they capture the tidal and subtidal seasonal cycles and do moderately well on the subtiddal temperature with the monthly anomaly subtracted. For salinity, CIOFS fresh shows moderate improvement over CIOFS hindcast.

[91MB zipfile of plots and stats files](https://files.axds.co/ciofs_fresh/zip/moorings.zip)

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
from dateparser.search import search_dates
from bokeh.models import FixedTicker
import holoviews as hv
import os
from pathlib import Path
import subprocess


ins_type = "moorings"  # instrument name
models = ["ciofs3"]

years = [1999, 2000, 2001, 2006, 2007, 2008, 2009, 2010, 2014, 2015, 2016, 
         2017, 2018, 2019, 2020]

# can only do these when running in docker with playwright available
# once they exist, can run outside of docker because don't need to
# recreate the png files
run_pdf = True
```

```{code-cell} ipython3
:tags: [remove-input]

def save_png(abs_path, figname):
    if not run_pdf:
        print("Skipping PNG creation because run_pdf is False")
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

slugs = [        "moorings_aoos_cdip",
        "moorings_circac",
        "moorings_kbnerr",
        "moorings_kbnerr_bear_cove_seldovia",
        "moorings_kbnerr_historical",
        "moorings_kbnerr_homer",
        "moorings_noaa",
        "moorings_nps",
        "moorings_uaf",
        ]
slug_names = {"moorings_aoos_cdip": "AOOS CDIP",
              "moorings_circac": "CIRCAC",
              "moorings_kbnerr": "KBNERR",
              "moorings_kbnerr_bear_cove_seldovia": "KBNERR Seldovia",
              "moorings_kbnerr_historical": "KBNERR Historical",
              "moorings_kbnerr_homer": "KBNERR Homer",
              "moorings_noaa": "NOAA",
                "moorings_nps": "NPS",
              "moorings_uaf": "UAF",
              }
rows = []
icount = 1
icount2 = 1
icount3 = 1
source_names_present = {}
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = list(cat)
    source_names_present[slug] = []
    for source_name in source_names:
        lon, lat = cat[source_name].metadata["minLongitude"], cat[source_name].metadata["minLatitude"]
        minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
        # data_time_range = DateTimeRange(minTime, maxTime)
        # not data_time_range.is_intersection(model_time_range)
        if not station_intersect_with_years(minTime, maxTime):
            # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
            continue
        # print(f"Adding {source_name} because min time {minTime} and max time {maxTime} are in {years}")
        source_names_present[slug].append(source_name)
        if "moorings_kbnerr_homer" in slug or "moorings_kbnerr_historical" in slug:
            # print(icount, source_name)
            if np.mod(icount, 2) == 0:  # even
                lat += icount*0.0025
            elif np.mod(icount, 2) == 1:  # odd
                lat -= icount*0.0025
            icount += 1
        elif "moorings_kbnerr_bear_cove" in slug:
            lat += icount2*0.0025
            icount2+= 1
        elif slug == "moorings_kbnerr":
            lat += icount3*0.0025            
            icount3+= 1
        start_time = pd.Timestamp(cat[source_name].metadata["minTime"])
        end_time = pd.Timestamp(cat[source_name].metadata["maxTime"])
        rows.append([source_name, lon, lat, start_time, end_time, slug, slug_names[slug]])
df = pd.DataFrame(rows, columns=["station","lon","lat","start_time", "end_time", "slug", "slug_name"])
```

```{code-cell} ipython3
:tags: [remove-input]

figname = f"build_figures/{ins_type}_map"
abs_path = os.path.abspath(f"{figname}.html")

fmap = df.hvplot.points(x="lon", y="lat", by="slug_name",
                legend="top_left", geo=True, tiles=True, size=50, hover_cols=["station","start_time","end_time"],
                coastline=False, xlabel="Longitude", ylabel="Latitude", title="Moorings",
                width=600, height=700, marker="o", fontscale=1.2, alpha=0.75)
if not Path(f"{figname}.png").exists():
    hv.save(fmap, figname, fmt='html')
    save_png(abs_path, figname)

glue("fig_map", fmap, display=False)
```

```{glue:figure} fig_map
:name: "fig-overview-moorings-map"

All mooring stations, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```

+++

````{div} full-width                
```{figure} build_figures/moorings_map.png
:name: "fig-overview-moorings-map"

All mooring stations, by project. (PNG screenshot, available for PDF and for saving image.)
```
````

+++

## Taylor Diagrams

Taylor diagrams summarize the skill of the two models in capturing the moorings datasets. The data has been grouped by region (Figs. {numref}`{number}<fig-moorings_by_region_ssh>`, {numref}`{number}<fig-moorings_by_region_temp>`, and {numref}`{number}<fig-moorings_by_region_salt>`). Sea surface height ({numref}`Fig. {number}<fig-moorings_by_region_ssh>`) is captured well by the models outside of Cook Inlet and in Upper Cook Inlet, but less well in Kachemak Bay. Both models have too low variance and correlation in capturing the subtidal sea surface height, but is better for CIOFS Fresh than Hindcast. Temperature ({numref}`Fig. {number}<fig-moorings_by_region_temp>`) is medium to well-captured in both models for the full and subtidal signals. For the subtidal anomaly, the models perform similarly to each other but none of the regions show good performance. Salinity time series ({numref}`Fig. {number}<fig-moorings_by_region_salt>`) are poorly captured across the board for both models. Skill scores are shown in the next plots for each dataset.


```{figure} ../figures/taylor_diagrams/moorings_by_region_ssh.png
---
name: fig-moorings_by_region_ssh
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for sea surface height: full signal minus the mean (left) and subtidal, grouped by region of Cook Inlet, for moorings.
```


```{figure} ../figures/taylor_diagrams/moorings_by_region_temp.png
---
name: fig-moorings_by_region_temp
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for temperature: full signal (left), subtidal (center), and subtidal (right) minus the monthly mean, grouped by region of Cook Inlet, for moorings.
```


```{figure} ../figures/taylor_diagrams/moorings_by_region_salt.png
---
name: fig-moorings_by_region_salt
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for salinity: full signal (left), subtidal (center), and subtidal (right) minus the monthly mean, grouped by region of Cook Inlet, for moorings.
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, source_name, model_name, key_variable, which):
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = sorted(paths.OUT_DIR.glob(f"{slug}_{source_name}_{key_variable}{which}.yaml"))
    has_dates = False
    if len(stats_fnames) == 0:
        stats_fnames = sorted(paths.OUT_DIR.glob(f"{slug}_{source_name}_{key_variable}_????-??-??_????-??-??{which}.yaml"))
        has_dates = True
        if len(stats_fnames) > 0:
            # import pdb; pdb.set_trace() #dparser.parse(stats_fnames[0].stem, fuzzy=True)
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore",
                    # message="Parsing dates involving a day of month without a y",
                    category=DeprecationWarning,
                )
                # print(f"len(stats_fnames) = {len(stats_fnames)}")
                # print([f.stem for f in stats_fnames])
                stats_fnames = [f for f in stats_fnames if search_dates(str(f), settings={"DATE_ORDER": "YMD"})[0][1].year in years]
                # print([f.stem for f in stats_fnames])
                # import pdb; pdb.set_trace()
    else:
        minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
        if not station_intersect_with_years(minTime, maxTime):
            import pdb; pdb.set_trace()
            # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
            return [], has_dates
    return stats_fnames, has_dates

def load_ss(index, stats_fnames, model_name, key_variable):
    ds = pd.Series(index=index, dtype=float)
    for station, stats_fname in zip(index, stats_fnames):
        with open(stats_fname, "r") as stream:
            ss = yaml.safe_load(stream)["ss"]["value"]
            ds.loc[station] = ss
    return ds
```

```{code-cell} ipython3
:tags: [remove-input]

model_names, key_variables = models, ["ssh","temp","salt"]
whichs = ["_subtract-mean_subtidal", "_subtract-mean", "", "_subtidal_subtract-monthly-mean", "_subtidal"]

dfalls = []
all_slugs, all_slug_names, all_times = [], [], []
all_lons, all_lats = [], []
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    dfs = {}
    # stations_this_slug = df[df["slug"] == slug]["station"]
    # every source_name needs lons/lats
    slug_lons, slug_lats = {}, {}
    for model_name in model_names:
        for key_variable in key_variables:
            for which in whichs:
                dfouts = []
                have_counted = False
                for source_name in source_names_present[slug]:
                    stats_fnames, has_dates = return_paths(slug, source_name, model_name, key_variable, which)
                    baselon = df[df["station"] == source_name]["lon"].iloc[0]
                    baselat = df[df["station"] == source_name]["lat"].iloc[0]
                    if has_dates:
                        # make a station name to represent each year of comparison
                        source_name_years = [f"{source_name}: {stats_fname.stem.split(f'{key_variable}_')[1][:4]}" for stats_fname in stats_fnames] 
                        dfout = load_ss(source_name_years, stats_fnames, model_name, key_variable)
                        
                        if len(dfout) > 1:
                            # calculate lon/lat locations
                            nrows = np.ceil(np.sqrt(len(dfout)))
                            ncols = nrows
                            Dlon = 1  # max overall delta lon
                            Dlat = 0.5  # max overall delta lat
                            dlat = Dlat/(nrows-1)  # delta per point
                            dlon = Dlon/(nrows-1)

                            dlats = np.linspace(0, Dlat, int(nrows)) - dlat
                            dlons = np.linspace(0, Dlon, int(ncols)) - dlon

                            Dlons, Dlats = np.meshgrid(dlons, dlats)

                            lon = (baselon + Dlons).flatten()[:len(dfout)]
                            lat = (baselat + Dlats).flatten()[:len(dfout)]
                        else:
                            lon = [baselon]
                            lat = [baselat]
                        
                    else:
                        # import pdb; pdb.set_trace()
                        dfout = load_ss([source_name], stats_fnames, model_name, key_variable)
                        lon = [baselon]
                        lat = [baselat]

                    if (len(dfout) > 0) and (source_name not in slug_lons.keys()):
                        slug_lons[source_name] = lon
                        slug_lats[source_name] = lat
                        
                    
                    dfouts.append(dfout)
                
                dfs[f"{model_name}_{key_variable}_{which}"] = pd.concat(dfouts, axis=0)
                
    mindex = pd.MultiIndex.from_product([model_names, key_variables, whichs])
    dfs_concat = pd.concat(dfs, axis=1)
    data = dfs_concat.values
    slug_times = []
    for source_name in source_names_present[slug]:
        # print(slug, source_name)
        # years
        rows_for_source_name = dfs_concat.index[dfs_concat.index.str.contains(source_name)]
        # if source_name == "kacsewq":
        #     import pdb; pdb.set_trace()
        if len(rows_for_source_name) > 1:
            new_times = rows_for_source_name.str[-4:]
            slug_times.extend(new_times)  # grab years from names
        else:
            # import pdb; pdb.set_trace()
            new_times = [df[df["station"] == source_name]["start_time"].iloc[0]]
            slug_times.extend(new_times)
    
    all_slugs.extend([slug]*len(dfs_concat))
    all_slug_names.extend([slug_names[slug]]*len(dfs_concat))
    all_times.extend(slug_times)
    for source_name, lons in slug_lons.items():
        all_lons.extend(lons)
        # print(f"source name {source_name} in slug {slug} adding lons {lons}, len {len(lons)} ")
    for source_name, lats in slug_lats.items():
        all_lats.extend(lats)

    dfalltemp = pd.DataFrame(data, index=dfs_concat.index, columns=mindex)
    # print(f"dfs_concat index {dfs_concat.index}, len {len(dfs_concat.index)}")
    dfalls.append(dfalltemp)
dfall = pd.concat(dfalls, axis=0)
dfall.index.name = "station"

dfall["lon"] = all_lons
dfall["lat"] = all_lats
# dfall["date_time"] = all_times
dfall["slug"] = all_slugs
dfall["slug_name"] = all_slug_names
dfall = dfall.reset_index().set_index(["station","lon","lat","slug","slug_name"])
# dfall = dfall.reset_index().set_index(["station","lon","lat","date_time","slug"])
```

```{code-cell} ipython3
:tags: [remove-input]

newcmap = cmocean.cm.matter

hovers = [("Slug", "@slug_name"),
          ("Station", "@station"),
          ("Start Time", "@start_time"),
          ("End Time", "@end_time"),
          ("Longitude", "@lon"),
          ("Latitude", "@lat"),
          ("SS bin", "@ss_range"),
          ]
hover_cols = ["slug_name", "station", "start_time", "end_time", "lon", "lat", "ss_range"]

# inputs = dict(x="lon", y="lat", c="ss", hover=False, by="slug_name")
inputs = dict(x="lon", y="lat", c="ss_code", hover_cols=hover_cols, by="slug_name")
plot_kwargs = dict(geo=True, tiles=True, size=100, width=600, height=700, clim=(0,1), cmap=newcmap,
                #   coastline="10m", 
                  xlabel="Longitude", ylabel="Latitude", legend="top_left",
                  fontscale=1.25)

vardescs = {"temp": "Sea temperature", "salt": "Salinity", "ssh": "Sea surface height"}


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

def plot(model_name, key_variable, which, clabel, title):
    # clabel = f"Model skill scores for moorings for {vardesc}"
    # dfallsub = dfall.loc[:,(model_names,key_variable)]
    # dfallsub = dfall.loc[:,(model_names,key_variable,which)]
    # dfallsubsub = dfall.loc[:,(model_name,key_variable)].dropna().rename("ss")
    dfallsubsub = dfall.loc[:,(model_name,key_variable,which)].dropna().rename("ss")
    cats = pd.cut(dfallsubsub, cat_bins).to_frame()
    cats["ss_code"] = cats["ss"].cat.codes
    cats["ss_range"] = cats["ss"].astype(str)

    # we plot the category codes but then label the colorbar correctly
    # so we don't have to plot a continuous colorbar with many levels
    return cats.hvplot.points(**inputs, **plot_kwargs, title=title, clabel=clabel, alpha=1.0).opts(opts_pts)
```

```{code-cell} ipython3
:tags: [remove-input]

def make_figures(model, key_variable, which, clabel, titles):


    if isinstance(key_variable, list) and len(key_variable) > 1:
        figname = f"build_figures/{ins_type}_{key_variable[0]}{which[0]}"
        # figname = f"{ins_type}_{which}_{key_variable[0]}_{key_variable[1]}"
        plots = []
        for key_var, whi, clabel, title in zip(key_variable, which, clabel, titles):
            plots.append(plot(model, key_var, whi, clabel, title))

        if len(key_variable) == 2:
            variable_plot = plots[0] + plots[1]
        elif len(key_variable) == 3:
            variable_plot = plots[0] + plots[1] + plots[2]
    else:
        figname = f"build_figures/{ins_type}{which}_{key_variable}"
        variable_plot = plot(model, key_variable, which, clabel, titles)

    abs_path = os.path.abspath(f"{figname}.html")

    if not Path(f"{figname}.png").exists():
        hv.save(variable_plot, figname, fmt='html')
        save_png(abs_path, figname)

    return variable_plot, figname, abs_path
```

## Skill Scores

### Sea Surface Height

```{code-cell} ipython3
:tags: [remove-input]

key_variables, whiches = ["ssh", "ssh"], ['_subtract-mean', '_subtract-mean_subtidal']
titles = ["Sea surface height minus mean", "Subtidal sea surface height minus mean"]
clabels = [f"{models[0].upper()} model skill scores for moorings, {vardescs[key_variables[0]].lower()}, minus mean"]
clabels.append(f"{models[0].upper()} model skill scores for moorings, subtidal {vardescs[key_variables[1]].lower()}, minus mean")

ssh_plot, figname, abs_path = make_figures(models[0], key_variables, whiches, clabels, titles)
glue("ssh_plot", ssh_plot, display=False)
```

````{div} full-width   
```{glue:figure} ssh_plot
:name: "fig-overview-moorings-ssh"

Skill scores for CIOFSv3 with moorings for tidal (left) and subtidal (right) sea surface height with mean subtracted for moorings, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```
````

+++

```{figure} build_figures/moorings_ssh_subtract-mean.png
:name: "fig-overview-moorings-ssh"

Skill scores for CIOFSv3 with moorings for tidal (left) and subtidal (right) sea surface height with mean subtracted for moorings, by project. (PNG screenshot, available for PDF and for saving image.)
```

+++

### Temperature

+++

#### Full signal

```{code-cell} ipython3
:tags: [remove-input]

key_variables, whiches = "temp", ''
titles = "Sea temperature"
clabel = f"{models[0].upper()} model skill scores for moorings for {vardescs[key_variables].lower()}"

tidal_temp, figname, abs_path = make_figures(models[0], key_variables, whiches, clabel, titles)
glue("tidal_temp", tidal_temp, display=False)
```

````{div} full-width   
```{glue:figure} tidal_temp
:name: "fig-overview-moorings-tidal-temp"

Skill scores for CIOFSv3 with moorings for tidal sea temperature, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```
````

+++

```{figure} build_figures/moorings_temp.png
:name: "fig-overview-moorings-tidal-temp"

Skill scores for CIOFSv3 with moorings for tidal sea temperature, by project. (PNG screenshot, available for PDF and for saving image.)
```

+++

#### Subtidal

```{code-cell} ipython3
:tags: [remove-input]

key_variables, whiches = ["temp", "temp"], ['_subtidal', '_subtidal_subtract-monthly-mean']
titles = ["Subtidal sea temperature", "Subtidal sea temperature minus monthly mean"]

clabels = [f"{models[0].upper()} model skill scores for moorings for subtidal {vardescs[key_variables[0]].lower()}"]
clabels.append(f"{models[0].upper()} model skill scores for moorings for subtidal {vardescs[key_variables[1]].lower()} anomaly")

temp_plot_subtidal, figname, abs_path = make_figures(models[0], key_variables, whiches, clabels, titles)
glue("temp_plot_subtidal", temp_plot_subtidal, display=False)
```

````{div} full-width   
```{glue:figure} temp_plot_subtidal
:name: "fig-overview-moorings-subtidal-temp"

Skill scores for CIOFSv3 with moorings for subtidal temperature (left) and subtidal temperature anomaly (right), by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```
````

+++

```{figure} build_figures/moorings_temp_subtidal.png
:name: "fig-overview-moorings-subtidal-temp"

Skill scores for CIOFSv3 with moorings for subtidal temperature (left) and subtidal temperature anomaly (right), by project. (PNG screenshot, available for PDF and for saving image.)
```

+++

### Salinity

+++

#### Full signal

```{code-cell} ipython3
:tags: [remove-input]

key_variables, whiches = "salt", ''
titles = "Salinity"
clabel = f"{models[0].upper()} model skill scores for moorings for {vardescs[key_variables].lower()}"

tidal_salt, figname, abs_path = make_figures(models[0], key_variables, whiches, clabel, titles)
glue("tidal_salt", tidal_salt, display=False)
```

````{div} full-width   
```{glue:figure} tidal_salt
:name: "fig-overview-moorings-tidal-salt"

Skill scores for CIOFSv3 with moorings for tidal salinity, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```
````

+++

```{figure} build_figures/moorings_salt.png
:name: "fig-overview-moorings-tidal-salt"

Skill scores for CIOFSv3 with moorings for tidal salinity, by project. (PNG screenshot, available for PDF and for saving image.)
```

+++

#### Subtidal

```{code-cell} ipython3
:tags: [remove-input]

key_variables, whiches = ["salt", "salt"], ['_subtidal', '_subtidal_subtract-monthly-mean']
titles = ["Subtidal salinity", "Subtidal salinity minus monthly mean"]

clabels = [f"{models[0].upper()} model skill scores for moorings for subtidal {vardescs[key_variables[0]].lower()}"]
clabels.append(f"{models[0].upper()} model skill scores for moorings for subtidal {vardescs[key_variables[1]].lower()} anomaly")

salt_plot_subtidal, figname, abs_path = make_figures(models[0], key_variables, whiches, clabels, titles)
glue("salt_plot_subtidal", salt_plot_subtidal, display=False)
```

````{div} full-width   
```{glue:figure} salt_subtidal
:name: "fig-overview-moorings-subtidal-salt"

Skill scores for CIOFSv3 with moorings for subtidal salinity (left) and subtidal salinity anomaly (right), by project. Click on a legend entry to toggle the transparency.
```
````

+++

```{figure} build_figures/moorings_salt_subtidal.png
:name: "fig-overview-moorings-subtidal-salt"

Skill scores for CIOFSv3 with moorings for subtidal salinity (left) and subtidal salinity anomaly (right), by project. (PNG screenshot, available for PDF and for saving image.)
```

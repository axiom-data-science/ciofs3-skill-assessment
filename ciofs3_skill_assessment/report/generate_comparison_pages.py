"""Generate the model-data comparison notebooks to be turned into pages."""


import subprocess
import intake
import nbformat as nbf
# import ciofs_hindcast_report as chr
import pandas as pd
import ocean_model_skill_assessor as omsa
from datetimerange import DateTimeRange
import numpy as np
import pathlib
import cf_pandas as cfp
import report_utils.page_utils as pu
import more_utils as mu
import cook_inlet_catalogs as cic
import report_utils.utils as utils
from datetimerange import DateTimeRange

# define these in more_utils
# models = ["ciofs_hindcast"]#, "ciofs_freshwater"]
key_variables = ["ssh", "temp", "salt", "along", "across", "speed"]

years = [2003, 2004, 2005, 2006, 2012, 2013, 2014]

## For CTD transects
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
        "ctd_transects_otf_kbnerr": ['2003-07-01'],
        "ctd_transects_uaf": ['Transect_01'], 
        "hfradar": ['lower-ci_system-B_2006-2007', 'upper-ci_system-A_2002-2003', 'upper-ci_system-A_2009']
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
        "hfradar": ['Lower Cook Inlet System B (2006-2007)','Upper Cook Inlet System A (2002-2003)','Upper Cook Inlet System A (2009)']
               }



def map_cell(slug):
    
    # map cell
    code = f"""\
cat = intake.open_catalog(cic.utils.cat_path("{slug}"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
"""
    codecell = nbf.v4.new_code_cell(code)
    codecell['metadata']['tags'] = ["remove-input"]
    return codecell


def map_cell_ctd_transects(slug):
    """Create a map cell for CTD transects."""
    # map cell
    code = f"""\
cat = intake.open_catalog(cic.utils.cat_path("{slug}"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join({source_names[slug]}))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = {line_names[slug]}
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
"""
    codecell = nbf.v4.new_code_cell(code)
    codecell['metadata']['tags'] = ["remove-input"]
    return codecell


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

def generate_page(slug, not_in_jupyter_book):   

    for model in mu.models:
        paths = omsa.paths.Paths(mu.project_name(slug, model))
        here = mu.outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = list(cat)
    
    nb = nbf.v4.new_notebook()

    ## INITIAL STUFF

    text = f"""\
# {cat.metadata['overall_desc']}

* {slug}

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/{slug}.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/{slug}.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.
"""

    # Add these cells to the notebook
    nb['cells'] = [pu.imports_cell(),
                   nbf.v4.new_markdown_cell(text),
                #    nbf.v4.new_code_cell(code),
                   ]

#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`
    # Add map markdown cell
    nb['cells'].append(map_cell(slug))
    # nb['cells'].extend([map_cell(slug, cat.metadata["map_description"], label="", caption=""),])
    
    ## Overall summary of statistics
    dfstats = mu.aggregate_overall_stats(slug)
    # import pdb; pdb.set_trace()
    cols_to_use = ["source_name","ciofs_hindcast"]
    if "ciofs_fresh" in dfstats.columns:
        cols_to_use.append("ciofs_fresh")
    dfstats_by_heading = dfstats.reset_index().set_index(["key_variable","ts_mods"]).sort_index()[cols_to_use]
    
    
    for ind in dfstats_by_heading.index.unique():
        key_variable, ts_mods = ind[0], ind[1]
        figname = mu.COMP_PAGE_DIR(slug) / f"{slug}_{key_variable}_{ts_mods}.png"
        df_to_plot = dfstats_by_heading.loc[ind]
        if isinstance(df_to_plot, pd.Series):
            df_to_plot = df_to_plot.to_frame().transpose().reset_index(drop=True).set_index("source_name")
        else:
            df_to_plot = df_to_plot.reset_index(drop=True).set_index("source_name")
    
    df = mu.aggregate_stats(slug)
    # drop slug as an index
    df = df.reset_index().set_index(["source_name","key_variable","ts_mods"])

    ## Loop over source names
    for source_name in source_names:
        
        source_md_0 = f"""\
## {source_name}

"""

        for model in mu.models:
            data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
            data_min_time, data_max_time = pd.Timestamp(data_min_time.replace("Z","")), pd.Timestamp(data_max_time.replace("Z",""))
                

        if source_name not in df.index:  # check if source_name is in the model output
            continue

        nb['cells'].extend([nbf.v4.new_markdown_cell(source_md_0),])
        
        # find all unique combinations of 'source_name', 'key_variable', 'ts_mods'
        for ind in df.loc[source_name].index.unique():
            key_variable, ts_mods = ind[0], ind[1]
            
            # subset of df, 1 set of source_name, key_variable, and ts_mods
            dfs = df.loc[source_name].loc[ind]

            if dfs.ndim > 1:
                dfs["start_time"] = pd.to_datetime(dfs["start_time"])
                dfs["start_time"] = dfs["start_time"].dt.year
            
            # key_variable (0), ts_mods (1)
            text = f"""\
### {mu.translate_var(key_variable)}: {mu.translate(ts_mods)}
"""
            nb['cells'].extend([nbf.v4.new_markdown_cell(text),])

            if dfs.ndim > 1:
                # add heatmap for all years
                # slug, key_variable(0), ts_mods (1)
                figname = mu.COMP_PAGE_DIR(slug) / f"{slug}_{source_name}_{key_variable}_{ts_mods}.png"
                # import pdb; pdb.set_trace()
                # print(figname.name, len(dfs))
                
                
                # # KMT try without this
                # plot_source_stats(dfs.reset_index().set_index("start_time")[models], source_name, figname)
                # label = f"fig-{source_name}-{key_variable}-{ts_mods}"
                # caption = f"Skill score by year for {translate_var(key_variable).lower()}, {translate(ts_mods)}"
                # text = utils.mk_fig_wide(figname.name, label, caption)
                # nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
                
                # if this is an anomaly calculation, show mean
                if "subtract-monthly-mean" in ts_mods:
                    dfd = cat[source_name].read()
                    figname = mu.COMP_PAGE_DIR(slug) / f"{slug}_{source_name}_{key_variable}_mean.png"
                    # import pdb; pdb.set_trace()
                    mu.plot_mean(dfd, dfd.cf[key_variable].name, figname)      
                    label = ""#f"fig-{source_name}-{key_variable}"
                    caption = ""#f"{translate_var(key_variable)} averaged monthly across data range with variation across years included."
                    text = utils.mk_fig_wide(figname.name, label, caption, not_in_jupyter_book)
                    nb['cells'].extend([nbf.v4.new_markdown_cell(text),])
                
            for model in mu.models:
                
                # if skip_nwgoa and model == "nwgoa":
                #     continue

                header = f"""\
#### {model.upper()}

"""
                
                # loop over 1 row or multiple years of figures for 
                # source_name, key_Variable, ts_mods combination
                if isinstance(dfs, pd.Series):
                    dfs = dfs.to_frame().T

                if len(dfs) > 1 and not not_in_jupyter_book:

                    header += """

`````{dropdown} Comparison plots by year

"""
                    
                for row in dfs.iterrows():
                    row = row[1]
                    
                    # row might be mostly nan's if it is present for one model but not the other
                    # in which case, skip
                    if model in row.index and pd.isnull(row[model]):
                        continue
                    
                    if len(dfs) > 1:
                        header += f"""\
##### {row["start_time"]}

"""

                    if isinstance(row[f'path_{model}'], pathlib.Path):
                        path = row[f'path_{model}'].with_suffix('.png').relative_to(mu.COMP_PAGE_DIR(slug))
                    elif np.isnan(row[f'path_{model}']):
                        continue
                    label = ""#f"fig-{model}-{source_name}-{key_variable}-{ts_mods}"
                    caption = ""#f"Model-data comparison for {source_name} of {translate_var(key_variable).lower()}"
                    # if len(dfs) > 1:
                    #     label += f"-{row['start_time']}"
                    #     caption += f" for {row ['start_time']}"
                    header += utils.mk_fig_wide(path, label, caption, not_in_jupyter_book)

                if len(dfs) > 1 and not not_in_jupyter_book:
                    header += """

`````
"""


                nb['cells'].extend([nbf.v4.new_markdown_cell(header),])

    file = f'{mu.COMP_PAGE_DIR(slug) / slug}.ipynb'
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])
    
    
def overview_hfradar(not_in_jupyter_book):
    
    slug = "hfradar"
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    # source_names = list(cat)
    source_names = ["lower-ci_system-B_2006",
                    "upper-ci_system-A_2003"]
    # source_names = ["lower-ci_system-B_2006-2007",
    #                 "upper-ci_system-A_2002-2003"]

    # #symlink in map from data comp dir
    # there = mu.COMP_PAGE_DIR(slug) / f"map_of_{slug}.png"
    # here = mu.COMP_PAGE_DIR("overview_hfradar") / f"map_of_{slug}.png"
    # if not here.exists():
    #     here.symlink_to(there)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:overview_hfradar)=
# Overview HF Radar Data

Detailed model-data comparison page: {{ref}}`HF Radar model-data comparison page <page:{slug}-comparison>`

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/{slug}.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/{slug}.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

[8MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/hfradar.zip)
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(map_cell_ctd_transects(slug))

    ## Loop over models first
    for model_name in mu.models:
        
        nb['cells'].append(pu.text_cell(pu.header_text(model_name.upper(), header=2)))

        for source_name in source_names:
            # data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
            nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=3)))

            text = ""
            for which in ["tidal","subtidal"]:
                text += pu.header_text(which.capitalize(), header=4)
                # loc = mu.COMP_PAGE_DIR(slug) / f"{slug}_{model_name}" / f"{slug}_{source_name}_{model_name}_{which}.png"
                # loc = mu.COMP_PAGE_DIR("overview_hfradar") / f"{slug}_{source_name}_{model_name}_{which}.png"
                loc = mu.COMP_PAGE_DIR("overview_hfradar") / f"{slug}_{source_name}_{model_name}_{which}.png"
                # loc.relative_to(pathlib.Path("."))
                # loc = loc.relative_to(mu.COMP_PAGE_DIR("overview_hfradar"))
                label = f"fig-overview-hfradar-{source_name}-{model_name}-{which}"
                caption = f"{which.capitalize()} surface currents skill score for {model_name.upper()} and dataset {source_name}"
                text += utils.mk_fig_wide(loc, label, caption, not_in_jupyter_book)
            nb['cells'].append(pu.text_cell(text))
    
    file = "overview_hfradar.ipynb"
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])
    
    
def hfradar(slug, not_in_jupyter_book):   

    cat = intake.open_catalog(cic.utils.cat_path(slug))

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in mu.models:
        paths = omsa.paths.Paths(mu.project_name(slug, model))
        here = mu.outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.metadata['overall_desc']}

* {slug}

See the full dataset page for more information: {{ref}}`page:{slug}`

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.
"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(map_cell_ctd_transects(slug))
    # nb['cells'].append(map_cell(slug, cat.metadata["map_description"], label="", caption=""))


    # TIDAL ELLIPSES #
    source_names = [
                    "lower-ci_system-B_2006",
                    "upper-ci_system-A_2003",
                    # "lower-ci_system-B_2006-2007",
                    # "upper-ci_system-A_2002-2003",
                    ]
    ## Loop over source names
    for source_name in source_names:
        
        # data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))        
        
        # Single Plots
        which_plot = ["M2 Tidal Ellipses", "K1 Tidal Ellipses", ]
        filesuffixs = [
                    "_M2_ellipses.png",
                    "_K1_ellipses.png",
        ]

        for plot, filesuffix in zip(which_plot, filesuffixs):
            nb['cells'].append(pu.text_cell(pu.header_text(plot, header=3)))
            
            for model in mu.models:
                nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=4)))

                text = ""
                
                caption = f"{plot.capitalize()} from surface currents for {model.upper()} and dataset {source_name}"
                loc = mu.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}{filesuffix}"
                loc = loc.relative_to(mu.COMP_PAGE_DIR(slug))
                label = f"fig-{source_name}-{model}-{'_'.join(which_plot)}"
                text += utils.mk_fig_wide(loc, label, caption, not_in_jupyter_book)
                nb['cells'].append(pu.text_cell(text))


    # OTHER PLOTS # 
    source_names = [
                    # "lower-ci_system-B_2006",
                    # "upper-ci_system-A_2003",
                    "lower-ci_system-B_2006-2007",
                    "upper-ci_system-A_2002-2003",
                    ]
    ## Loop over source names
    for source_name in source_names:
        
        # data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))        
        
        # Single Plots
        which_plot = ["Subtidal Mean", "Hourly", "Subtidal, 6-Hourly"]
        filesuffixs = [
                    "_east_north_remove-under-50-percent-data_units-to-meters_subtidal_mean.png",
                    "_east_north_remove-under-50-percent-data_units-to-meters.mp4", 
                    "_east_north_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H.mp4",
        ]

        for plot, filesuffix in zip(which_plot, filesuffixs):
            nb['cells'].append(pu.text_cell(pu.header_text(plot, header=3)))

            if "2006" in source_name and "east_north" in filesuffix:
                datestr = "2006-11-12_2007-01-01"
                filesuffix = f"_east_north_{datestr}_{filesuffix.split('_east_north_')[-1]}"
            elif "2002" in source_name and "east_north" in filesuffix:
                datestr = "2003-01-01_2003-06-09"
                filesuffix = f"_east_north_{datestr}_{filesuffix.split('_east_north_')[-1]}"
            
            for model in mu.models:
                nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=4)))

                text = ""
                
                caption = f"{plot.capitalize()} from surface currents for {model.upper()} and dataset {source_name}"
                if ".mp4" in filesuffix:
                    loc = f"hfradar_{model}/{slug}_{source_name}{filesuffix}"
                    # loc = f"https://files.axds.co/ciofs/hfradar_{model}/{slug}_{source_name}{filesuffix}"
                    label = f"fig-{source_name}-{model}-{plot}"
                    text += utils.mk_video_wide(loc, label, caption, not_in_jupyter_book)

                else:
                    loc = mu.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}{filesuffix}"
                    loc = loc.relative_to(mu.COMP_PAGE_DIR(slug))
                    label = f"fig-{source_name}-{model}-{'_'.join(which_plot)}"
                    text += utils.mk_fig_wide(loc, label, caption, not_in_jupyter_book)
                nb['cells'].append(pu.text_cell(text))


    # TIDAL CONSTANT #        
    source_names = [
                    "lower-ci_system-B_2006",
                    "upper-ci_system-A_2003",
                    # "lower-ci_system-B_2006-2007",
                    # "upper-ci_system-A_2002-2003",
                    ]
    ## Loop over different source names
    for source_name in source_names:
        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))        
        # Dropdowns of Plots
        nb['cells'].append(pu.text_cell(pu.header_text("Tidal Constants", header=3)))
        
        tidecons = ["M2","K1","S2","N2","O1","Q1","K2","P1"]
        # whichs = ["major","minor", "inclination", "phase"]
        which_plots = ["Major Amplitude", "Minor Amplitude", "Phase", "Inclination"]
        
        for model in mu.models:

            text = ""
            
            if not not_in_jupyter_book:
                text = f"""
`````{{dropdown}} {model.upper()}
"""
            for which_plot in which_plots:
                text += pu.header_text(which_plot, 3)
                
                for tidecon in tidecons:
                    which_name = which_plot.split()[0].lower()
                    loc = mu.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}_{tidecon}-{which_name}.png"
                    if loc.is_file():  # some tidal constants weren't run
                        loc = loc.relative_to(mu.COMP_PAGE_DIR(slug))
                        label = ""  #f"fig-{source_name}-{model}-{tidecon}-{which_name}"
                        caption = ""  #f"{tidecon} {which_plot.lower()} from surface currents for {model.upper()} and dataset {source_name}"
                        text += utils.mk_fig_wide(loc, label, caption, not_in_jupyter_book)
            
            if not not_in_jupyter_book:
                text += """

`````
"""
            nb["cells"].append(pu.text_cell(text))

    file = f'{mu.COMP_PAGE_DIR(slug) / slug}.ipynb'
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])
    
    
def adcp(slug, not_in_jupyter_book):   

    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = list(cat)
    source_names = [source_name for source_name in source_names if "0301" not in source_name and "0303" not in source_name]

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in mu.models:
        paths = omsa.paths.Paths(mu.project_name(slug, model))
        here = mu.outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.metadata['overall_desc']}

* {slug}

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/{slug}.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/{slug}.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    # Add map markdown cell
    nb['cells'].append(map_cell(slug))

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
        if not station_intersect_with_years(data_min_time, data_max_time):
            continue

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))
        
        for which_tidal in ["tidal","subtidal"]:

            nb['cells'].append(pu.text_cell(pu.header_text(which_tidal.capitalize(), header=3)))
            
            varnames = ["speed_rotate", "east_rotate", "north_rotate"]
            # varnames = ["speed", "along", "across"]
            vardescs = ["Horizontal Speed", "Along-Channel Velocity", "Across-Channel Velocity"]
            for varname, vardesc in zip(varnames, vardescs):

                nb['cells'].append(pu.text_cell(pu.header_text(vardesc.capitalize(), header=4)))

                for model in mu.models:
                    nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=5)))

                    text = ""
                    
                    caption = ""  # f"{which_tidal.capitalize()} {vardesc.lower()} from moored ADCP for {model.upper()} and dataset {source_name}"
                    loc = mu.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name}_{varname}"
                    if which_tidal == "subtidal":
                        loc = pathlib.Path(str(loc) + "_subtidal")
                    loc = loc.with_suffix(".png")
                    loc = loc.relative_to(mu.COMP_PAGE_DIR(slug))
                    label = ""  #f"fig-{source_name}-{model}-{varname}-{which_tidal}"
                    text += utils.mk_fig_wide(loc, label, caption, not_in_jupyter_book)
                    nb['cells'].append(pu.text_cell(text))


    file = f'{mu.COMP_PAGE_DIR(slug) / slug}.ipynb'
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])
    
    
def ctd_transects(slug, not_in_jupyter_book):   

    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = list(cat)

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in mu.models:
        paths = omsa.paths.Paths(mu.project_name(slug, model))
        here = mu.outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.metadata['overall_desc']}

* {slug}

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/{slug}.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/{slug}.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`

    nb['cells'].append(map_cell_ctd_transects(slug))

    # Add map markdown cell
    # nb['cells'].append(map_cell(slug, cat.metadata["map_description"], label="", caption=""))

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
        if not station_intersect_with_years(data_min_time, data_max_time):
            continue
        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))
        
        varnames = ["temp","salt"]
        vardescs = ["Sea Temperature [C]", "Salinity"]
        for varname, vardesc in zip(varnames, vardescs):

            nb['cells'].append(pu.text_cell(pu.header_text(vardesc, header=3)))

            for model in mu.models:
                nb['cells'].append(pu.text_cell(pu.header_text(model.upper(), header=4)))

                text = ""
                
                caption = ""  # f"{which_tidal.capitalize()} {vardesc.lower()} from moored ADCP for {model.upper()} and dataset {source_name}"
                loc = mu.COMP_PAGE_DIR(slug) / f"{slug}_{model}" / f"{slug}_{source_name.replace(' ', '_')}_{varname}"
                loc = loc.with_suffix(".png")
                loc = loc.relative_to(mu.COMP_PAGE_DIR(slug))
                label = ""  #f"fig-{source_name}-{model}-{varname}-{which_tidal}"
                text += utils.mk_fig_wide(loc, label, caption, not_in_jupyter_book)
                nb['cells'].append(pu.text_cell(text))

    file = f'{mu.COMP_PAGE_DIR(slug) / slug}.ipynb'
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])
    
    
def ctd_profiles(slug, not_in_jupyter_book):   

    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = list(cat)

    # link project out directories to comparison page dir so can use the 
    # images as relative paths
    for model in mu.models:
        paths = omsa.paths.Paths(mu.project_name(slug, model))
        here = mu.outdir(slug,model)
        if not here.exists():
            here.symlink_to(paths.OUT_DIR)
    
    nb = nbf.v4.new_notebook()
    nb['cells'] = [pu.imports_cell(),]

    text = f"""\
(page:{slug}-comparison)=
# {cat.metadata['overall_desc']}

* {slug}

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/{slug}.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/{slug}.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

"""

    nb['cells'].append(pu.text_cell(text))


#Then refer to the figure with {{numref}}`Figure {{number}}<fig-map>`
    # map cell
    nb['cells'].append(map_cell(slug))

#     code = f"""\
# cat = intake.open_catalog(cic.utils.cat_path("{slug}"))
# dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
# dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
# """
#     codecell = nbf.v4.new_code_cell(code)
#     codecell['metadata']['tags'] = ["remove-input"]
#     nb['cells'].append(codecell)

    ## Loop over source names
    for source_name in source_names:
        data_min_time, data_max_time = cat[source_name].metadata["minTime"], cat[source_name].metadata["maxTime"]
        if not station_intersect_with_years(data_min_time, data_max_time):
            continue

        nb['cells'].append(pu.text_cell(pu.header_text(source_name, header=2)))
        
        varnames = ["temp","salt"]
        vardescs = ["Sea Temperature [C]", "Salinity"]
        for varname, vardesc in zip(varnames, vardescs):

            nb['cells'].append(pu.text_cell(pu.header_text(vardesc, header=3)))

            text = ""
            
            caption = ""  # f"{which_tidal.capitalize()} {vardesc.lower()} from moored ADCP for {model.upper()} and dataset {source_name}"
            loc1 = mu.COMP_PAGE_DIR(slug) / f"{slug}_{mu.models[0]}" / f"{slug}_{source_name.replace('.','_')}_{varname}"
            loc1 = loc1.with_suffix(".png")
            loc2 = mu.COMP_PAGE_DIR(slug) / f"{slug}_{mu.models[1]}" / f"{slug}_{source_name.replace('.','_')}_{varname}"
            loc2 = loc2.with_suffix(".png")
            label = ""  #f"fig-{source_name}-{model}-{varname}-{which_tidal}"
            width = "49"
            if loc1.is_file():
                path = loc1.relative_to(mu.COMP_PAGE_DIR(slug))
                if not not_in_jupyter_book:
                    text += f"""
```{{image}} {path}
:width: {width}%
```
"""
                else:
                    text += utils.mk_md_fig(path, label, caption, width)

            if loc2.is_file():
                path = loc2.relative_to(mu.COMP_PAGE_DIR(slug))
                if not not_in_jupyter_book:
                    text += f"""
```{{image}} {path}
:width: {width}%
```
"""
                else:
                    text += utils.mk_md_fig(path, label, caption, width)

            nb['cells'].append(pu.text_cell(text))

    file = f'{mu.COMP_PAGE_DIR(slug) / slug}.ipynb'
    nbf.write(nb, file)

    # Run jupytext command
    subprocess.run(["jupytext", "--to", "myst", file])


# Generate comparison pages
if __name__ == "__main__":

    # True when running outside of Jupyter book framework
    # changes how plots are setup, removes dropdowns
    # overall removes some nice stuff that is only available in Jupyter book
    not_in_jupyter_book = False
    
    # slug = "hfradar"
    # hfradar(slug, not_in_jupyter_book)

    # overview_hfradar(not_in_jupyter_book)

    
    # slugs = [
    #      "ctd_transects_barabara_to_bluff_2002_2003",
    #     "ctd_transects_cmi_kbnerr", 
    #     "ctd_transects_cmi_uaf",
    #     "ctd_transects_gwa", 
    #     "ctd_transects_otf_kbnerr",
    #     "ctd_transects_uaf",  
    #          ]
    # for slug in slugs:
    #     print(slug)
    #     ctd_transects(slug, not_in_jupyter_book)

    # slugs = [
    #     "ctd_profiles_2005_noaa",
    #     "ctd_profiles_kachemack_kuletz_2005_2007",
    #     "ctd_profiles_kb_small_mesh_2006",
    #          ]
    # for slug in slugs:
    #     print(slug)
    #     ctd_profiles(slug, not_in_jupyter_book)

    slugs = [
        # "adcp_moored_noaa_coi_2005",
             "adcp_moored_noaa_coi_other",
             ]
    for slug in slugs:
        adcp(slug, not_in_jupyter_book)


    # slugs = [
    #     "moorings_aoos_cdip",
    #     "moorings_circac",
    #     "moorings_kbnerr",
    #     "moorings_kbnerr_bear_cove_seldovia",
    #     "moorings_kbnerr_historical", 
    #     "moorings_kbnerr_homer",
    #     "moorings_noaa",
    #     "moorings_uaf",
    #     ]
    # for slug in slugs:
    #     print(slug)
    #     generate_page(slug, not_in_jupyter_book)
    #     # if hasattr(generate_comparison_pages, slug):
    #     #     print(slug)
    #     #     getattr(generate_comparison_pages, slug)(slug)

import calendar
import yaml
import xarray as xr

from pathlib import Path
import report_utils.utils as utils
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import cf_pandas as cfp

models = ["ciofs_hindcast", "ciofs_fresh"]

def COMP_PAGE_DIR(slug):
    path = Path(slug)
    path.mkdir(parents=True, exist_ok=True)
    return path

def project_name(slug, model):
    return f"{slug}_{model}"

def outdir(slug, model):
    return COMP_PAGE_DIR(slug) / project_name(slug, model)

    
def translate(ts_mods):
    words = ""
    if isinstance(ts_mods, str):
    # if ts_mods is not None and not np.isnan(ts_mods):
        ts_mods = ts_mods.split("_")
        for ts_mod in ts_mods:
            if len(words) > 0:
                words += ", then "
            if ts_mod == "subtidal":
                words += "tidally-filtered"
            elif ts_mod == "subtract-monthly-mean":
                words += "monthly mean from data subtracted"
            elif ts_mod == "subtract-mean":
                words += "mean subtracted"
    return words
def translate_var(key_variable):
    if key_variable == "ssh":
        return "Sea surface height"
    if key_variable == "temp":
        return "Sea water temperature"
    if key_variable == "salt":
        return "Sea water salinity"
    if key_variable == "across":
        return "Across-channel velocity"
    if key_variable == "along":
        return "Along-channel velocity"
    if key_variable == "speed":
        return "Horizontal speed"


def aggregate_overall_stats(slug, source_names=None):

    dfmodels = []
    for model in models:
        print(model)
        statspaths = sorted(list(outdir(slug, model).glob(f"*.yaml")))
        all_desc = utils.group_decoded_paths(statspaths)
        all_desc = all_desc.set_index(['slug', 'source_name', 'key_variable', 'ts_mods']).sort_index()
        
        # loop over sets of indices defining different groupings of filenames
        dfsources = []
        for ind in all_desc.index.unique():
            paths = cfp.astype(all_desc.loc[ind, "path"], list)
            val = 0
            for path in paths:
                with open(path, "r") as stream:
                    stats = yaml.safe_load(stream)                    
                val += stats["ss"]["value"]
            val /= len(paths)  # change to mean
            dfsources.append(pd.DataFrame(index=[ind], data=val, columns=[model]))
        if len(dfsources)>0:
            dfmodels.append(pd.concat(dfsources, axis=0))
    if len(dfmodels)>0:
        dfstats = pd.concat(dfmodels, axis=1)
        if not isinstance(dfstats.index, pd.MultiIndex):
            dfstats.index = pd.MultiIndex.from_tuples(dfstats.index)
        dfstats.index.names = all_desc.index.names
    return dfstats.sort_index()


def plot_overall_stats(df, figname):
    figsize = (6,len(df)*.5)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    cbar_ax = fig.add_axes([0.95, 0.11, 0.02, 0.77])
    sns.heatmap(df, annot=True, linewidths=.5, vmin=0, vmax=1, cmap="cmo.matter_r", fmt='.2f', 
                cbar_ax=cbar_ax, ax=ax)#, cbar_kws=dict(pad=0.001))
    ax.tick_params(axis='both', which='major', labelsize=14, labelbottom = False, bottom=False, top = False, labeltop=True)
    ax.tick_params(axis='y', rotation=0)
    ax.set_ylabel("")
    fig.savefig(figname, dpi=100, bbox_inches="tight")
    plt.close(fig)


def plot_mean(df, varname, figname):
    monthly_mean = df[varname].groupby(df.cf["T"].dt.month).mean()
    # monthly_mean = df[varname].groupby(df.cf["T"].dt.month).mean()
    # unclear why I have to shift this
    monthly_mean_shifted = monthly_mean.copy()
    monthly_mean_shifted.index = monthly_mean_shifted.index - 1

    df = df.set_index(df.cf["T"].dt.month)
    # df = df.set_index(df.cf["T"].dt.month)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    sns.violinplot(data=df, x=df.index, y=varname, inner="quartile", color="orange")
    monthly_mean_shifted.plot(ax=ax, marker="o", color="k", figsize=(10,5))
    xticks = ax.get_xticklabels()
    ax.set_xticks(ax.get_xticks(), labels=[calendar.month_abbr[int(i.get_text())] for i in xticks])
    ax.set_xlabel("")
    ax.set_title("Monthly means and statistical variation over time")
    fig.savefig(figname, dpi=100, bbox_inches="tight")
    plt.close(fig)


def aggregate_stats(slug):

    dfmodels = []
    for model in models:
        statspaths = sorted(list(outdir(slug, model).glob(f"*.yaml")))
        all_desc = utils.group_decoded_paths(statspaths)        
        all_desc = all_desc.set_index(["source_name","key_variable","ts_mods","start_time"]).sort_index()
        
        # loop over each source and subsource to save mean skill score
        for ind in all_desc.index:
            path = all_desc.loc[ind, "path"]
            with open(path, "r") as stream:
                stats = yaml.safe_load(stream)
            all_desc.loc[ind,model] = stats["ss"]["value"]
        dfmodels.append(all_desc)
    if len(dfmodels)>0:
        dfstats = dfmodels[0]
        # import pdb; pdb.set_trace()
        if len(dfmodels)>1:
            full_index = dfmodels[0].index.union(dfmodels[1].index)
            dfstats = dfstats.reindex(full_index)
            dfstats.rename(columns={"path": f"path_{models[0]}"}, inplace=True)
            dfstats[f"path_{models[1]}"] = dfmodels[1]["path"]
        else:
            dfstats.rename(columns={"path": f"path_{models[0]}"}, inplace=True)
        # import pdb; pdb.set_trace()
        if len(dfmodels)>1 and not dfmodels[1].empty:
            dfstats["ciofs_fresh"] = dfmodels[1]["ciofs_fresh"]
    return dfstats.sort_index()


def plot_source_stats(df, source_name, figname):
    figsize = (6,len(df)*.5)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    cbar_ax = fig.add_axes([0.95, 0.11, 0.02, 0.77])
    sns.heatmap(df, annot=True, linewidths=.5, vmin=0, vmax=1, cmap="cmo.matter_r", fmt='.2f', 
                cbar_ax=cbar_ax, ax=ax)#, cbar_kws=dict(pad=0.001))
    ax.tick_params(axis='both', which='major', labelsize=14, labelbottom = False, bottom=False, top = False, labeltop=True)
    ax.tick_params(axis='y', rotation=0)
    ax.set_ylabel("")
    fig.suptitle(source_name, y=1.1)
    # plt.tight_layout()
    # import pdb; pdb.set_trace()
    fig.savefig(figname, dpi=100, bbox_inches="tight")
    plt.close(fig)

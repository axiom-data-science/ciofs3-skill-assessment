---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
---

```{code-cell}
:tags: [remove-input]

import intake
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
from IPython.display import Image, display
import cook_inlet_catalogs as cic
```

(page:overview_hfradar)=
# Overview HF Radar Data

The performance of the CIOFSv3 model for HF Radar data is summarized on this page. Shown below are a map of dataset locations, Taylor diagrams summarizing performance across the three CIOFS historical models, and overview maps showing markers colored to indicate the skill score of the model-data comparisons for each dataset.

Detailed model-data comparison page: {ref}`HF Radar model-data comparison page <page:hfradar-comparison>`

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/hfradar.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/hfradar.html).

* [11MB zipfile of plots](https://files.axds.co/ciofs3/zip/hfradar.zip)
* [14MB HF Radar model-data comparison as PDF](https://files.axds.co/ciofs3/pdfs/hfradar.pdf)

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("hfradar"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join(['lower-ci_system-B_2006-2007', 'upper-ci_system-A_2002-2003', 'upper-ci_system-A_2009']))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = ['Lower Cook Inlet System B (2006-2007)', 'Upper Cook Inlet System A (2002-2003)', 'Upper Cook Inlet System A (2009)']
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
```

## Taylor Diagrams

The present Taylor diagrams summarize the skill of the three historical CIOFS models in capturing the HF Radar datasets. Only datasets from years for which all three CIOFS historical models are available are used, which are 2003-2006 and 2012-2014 (the years modeled for CIOFS fresh).

The data has been grouped by region ({numref}`Fig. {number}<fig-hfradar_by_region_east>`) and season ({numref}`Fig. {number}<fig-hfradar_by_region_north>`). 
CIOFSv3 performs well (correlation coefficient $r\sim0.8$ and reasonable variance) for tidal north-south (approximately along-channel) HF Radar surface currents, but not as well ($r\sim0.3$ for lower Cook Inlet and $r\sim0.6$ for central Cook Inlet) for tidal east-west (approximately across-channel) currents. For subtidal currents, the north-south (along-channel) component is poorly captured, and east-west (across-channel) currents have some skill ($r\sim0.4$ for lower and central Cook Inlet). The three models perform similarly for all regions and variables.

```{figure} ../figures/taylor_diagrams/hfradar_by_region_east.png
---
name: fig-hfradar_by_region_east
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for east-west (approximately across-channel) tidal (left) and subtidal (right) velocities, grouped by region of Cook Inlet, for HF Radar datasets.
```


```{figure} ../figures/taylor_diagrams/hfradar_by_region_north.png
---
name: fig-hfradar_by_region_north
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars), CIOFS Fresh (triangles), and CIOFSv3 (circles) for north-south (approximately along-channel) tidal (left) and subtidal (right) velocities, grouped by region of Cook Inlet, for HF Radar datasets.
```

+++

## CIOFS3


+++

### lower-ci_system-B_2006-2007


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_lower-ci_system-B_2006-2007_ciofs3_tidal.png
---
name: fig-overview-hfradar-lower-ci_system-B_2006-2007-ciofs3-tidal
---
Tidal surface currents skill score for CIOFS3 and dataset lower-ci_system-B_2006-2007
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_lower-ci_system-B_2006-2007_ciofs3_subtidal.png
---
name: fig-overview-hfradar-lower-ci_system-B_2006-2007-ciofs3-subtidal
---
Subtidal surface currents skill score for CIOFS3 and dataset lower-ci_system-B_2006-2007
```
````


+++

### upper-ci_system-A_2002-2003


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2002-2003_ciofs3_tidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2002-2003-ciofs3-tidal
---
Tidal surface currents skill score for CIOFS3 and dataset upper-ci_system-A_2002-2003
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2002-2003_ciofs3_subtidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2002-2003-ciofs3-subtidal
---
Subtidal surface currents skill score for CIOFS3 and dataset upper-ci_system-A_2002-2003
```
````


+++

### upper-ci_system-A_2009


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2009_ciofs3_tidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2009-ciofs3-tidal
---
Tidal surface currents skill score for CIOFS3 and dataset upper-ci_system-A_2009
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2009_ciofs3_subtidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2009-ciofs3-subtidal
---
Subtidal surface currents skill score for CIOFS3 and dataset upper-ci_system-A_2009
```
````

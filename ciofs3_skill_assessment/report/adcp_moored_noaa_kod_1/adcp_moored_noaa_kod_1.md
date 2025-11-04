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

(page:adcp_moored_noaa_kod_1-comparison)=
# Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 1

* adcp_moored_noaa_kod_1

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/adcp_moored_noaa_kod_1.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/adcp_moored_noaa_kod_1.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("adcp_moored_noaa_kod_1"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## KOD0901


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0901_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0901_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0901_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0901_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0901_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0901_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0902


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0902_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0902_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0902_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0902_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0902_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0902_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0903


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0903_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0903_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0903_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0903_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0903_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0903_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0904


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0904_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0904_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0904_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0904_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0904_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0904_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0905


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0905_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0905_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0905_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0905_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0905_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0905_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0906


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0906_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0906_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0906_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0906_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0906_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0906_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0907


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0907_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0907_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0907_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0907_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0907_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0907_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0910


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0910_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0910_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0910_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0910_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0910_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0910_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0911


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0911_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0911_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0911_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0911_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0911_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0911_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0912


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0912_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0912_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0912_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0912_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0912_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0912_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0913


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0913_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0913_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0913_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0913_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0913_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0913_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0921


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0921_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0921_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0921_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0921_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0921_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0921_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0922


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0922_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0922_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0922_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0922_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0922_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0922_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0923


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0923_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0923_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0923_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0923_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0923_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0923_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0924


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0924_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0924_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0924_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0924_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0924_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0924_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0925


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0925_speed_rotate.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0925_east_rotate.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0925_north_rotate.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0925_speed_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0925_east_rotate_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_1_ciofs3/adcp_moored_noaa_kod_1_KOD0925_north_rotate_subtidal.png
---
name: 
---

```
````

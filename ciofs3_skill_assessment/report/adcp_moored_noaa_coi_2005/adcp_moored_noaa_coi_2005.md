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

(page:adcp_moored_noaa_coi_2005-comparison)=
# Moored ADCP (NOAA): ADCP survey Cook Inlet 2005

* adcp_moored_noaa_coi_2005

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/adcp_moored_noaa_coi_2005.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/adcp_moored_noaa_coi_2005.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("adcp_moored_noaa_coi_2005"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## COI0501


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0501_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0501_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0501_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0501_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0501_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0501_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0502


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0502_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0502_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0502_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0502_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0502_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0502_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0503


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0503_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0503_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0503_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0503_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0503_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0503_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0504


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0504_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0504_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0504_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0504_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0504_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0504_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0505


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0505_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0505_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0505_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0505_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0505_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0505_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0506


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0506_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0506_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0506_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0506_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0506_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0506_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0507


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0507_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0507_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0507_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0507_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0507_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0507_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0508


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0508_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0508_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0508_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0508_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0508_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0508_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0509


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0509_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0509_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0509_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0509_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0509_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0509_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0510


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0510_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0510_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0510_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0510_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0510_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0510_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0511


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0511_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0511_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0511_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0511_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0511_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0511_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0512


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0512_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0512_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0512_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0512_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0512_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0512_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0513


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0513_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0513_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0513_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0513_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0513_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0513_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0514


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0514_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0514_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0514_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0514_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0514_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0514_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0515


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0515_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0515_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0515_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0515_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0515_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0515_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0516


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0516_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0516_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0516_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0516_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0516_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0516_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0517


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0517_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0517_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0517_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0517_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0517_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0517_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0518


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0518_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0518_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0518_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0518_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0518_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0518_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0519


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0519_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0519_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0519_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0519_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0519_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0519_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0520


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0520_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0520_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0520_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0520_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0520_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0520_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0521


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0521_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0521_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0521_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0521_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0521_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0521_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0522


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0522_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0522_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0522_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0522_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0522_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0522_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0523


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0523_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0523_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0523_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0523_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0523_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0523_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0524


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0524_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0524_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0524_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0524_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0524_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_2005_ciofs3/adcp_moored_noaa_coi_2005_COI0524_north_rotate_subtidal.png
---
name: 
---

```
````

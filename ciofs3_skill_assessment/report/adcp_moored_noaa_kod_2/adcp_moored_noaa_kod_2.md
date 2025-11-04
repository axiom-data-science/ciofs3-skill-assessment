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

(page:adcp_moored_noaa_kod_2-comparison)=
# Moored ADCP (NOAA): ADCP survey Kodiak Island, Set 2

* adcp_moored_noaa_kod_2

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/adcp_moored_noaa_kod_2.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/adcp_moored_noaa_kod_2.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("adcp_moored_noaa_kod_2"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## KOD0926


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0926_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0926_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0926_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0926_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0926_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0926_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0927


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0927_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0927_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0927_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0927_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0927_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0927_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0928


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0928_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0928_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0928_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0928_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0928_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0928_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0929


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0929_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0929_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0929_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0929_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0929_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0929_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0930


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0930_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0930_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0930_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0930_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0930_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0930_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0931


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0931_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0931_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0931_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0931_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0931_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0931_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0932


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0932_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0932_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0932_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0932_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0932_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0932_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0933


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0933_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0933_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0933_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0933_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0933_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0933_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0934


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0934_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0934_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0934_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0934_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0934_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0934_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0935


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0935_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0935_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0935_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0935_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0935_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0935_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0936


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0936_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0936_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0936_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0936_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0936_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0936_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0937


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0937_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0937_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0937_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0937_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0937_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0937_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0938


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0938_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0938_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0938_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0938_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0938_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0938_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0939


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0939_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0939_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0939_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0939_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0939_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0939_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0940


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0940_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0940_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0940_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0940_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0940_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0940_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0941


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0941_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0941_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0941_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0941_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0941_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0941_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0942


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0942_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0942_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0942_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0942_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0942_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0942_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0943


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0943_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0943_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0943_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0943_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0943_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0943_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## KOD0944


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0944_speed_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0944_east_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0944_north_rotate.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0944_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0944_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_kod_2_ciofs3/adcp_moored_noaa_kod_2_KOD0944_north_rotate_subtidal.png
---
name: 
---

```
````

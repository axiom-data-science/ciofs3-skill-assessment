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

(page:adcp_moored_noaa_coi_other-comparison)=
# Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years

* adcp_moored_noaa_coi_other

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/adcp_moored_noaa_coi_other.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/adcp_moored_noaa_coi_other.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("adcp_moored_noaa_coi_other"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## COI0206


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0206_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0206_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0206_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0206_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0206_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0206_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0207


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0207_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0207_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0207_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0207_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0207_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0207_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0213


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0213_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0213_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0213_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0213_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0213_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0213_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0302


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0302_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0302_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0302_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0302_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0302_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0302_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0306


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0306_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0306_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0306_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0306_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0306_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0306_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0307


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0307_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0307_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0307_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0307_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0307_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0307_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0418


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0418_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0418_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0418_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0418_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0418_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0418_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0419


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0419_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0419_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0419_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0419_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0419_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0419_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0420


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0420_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0420_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0420_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0420_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0420_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0420_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0421


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0421_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0421_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0421_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0421_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0421_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0421_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0422


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0422_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0422_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0422_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0422_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0422_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0422_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0801


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0801_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0801_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0801_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0801_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0801_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0801_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI0802


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0802_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0802_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0802_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0802_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0802_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI0802_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1201


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1201_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1201_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1201_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1201_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1201_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1201_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1202


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1202_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1202_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1202_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1202_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1202_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1202_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1203


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1203_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1203_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1203_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1203_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1203_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1203_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1204


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1204_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1204_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1204_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1204_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1204_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1204_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1205


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1205_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1205_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1205_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1205_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1205_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1205_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1207


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1207_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1207_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1207_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1207_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1207_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1207_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1208


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1208_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1208_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1208_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1208_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1208_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1208_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1209


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1209_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1209_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1209_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1209_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1209_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1209_north_rotate_subtidal.png
---
name: 
---

```
````


+++

## COI1210


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS3


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1210_speed_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1210_east_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1210_north_rotate.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1210_speed_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1210_east_rotate_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs3/adcp_moored_noaa_coi_other_COI1210_north_rotate_subtidal.png
---
name: 
---

```
````

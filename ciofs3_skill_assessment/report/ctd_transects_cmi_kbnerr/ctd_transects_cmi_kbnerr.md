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

(page:ctd_transects_cmi_kbnerr-comparison)=
# CTD Transects, Moored CTD (CMI KBNERR): Six repeat, one single transect, one moored CTD

* ctd_transects_cmi_kbnerr

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_cmi_kbnerr.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_cmi_kbnerr.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_cmi_kbnerr"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join(['Cruise_14-Line_1', 'Cruise_14-Line_2', 'Cruise_14-Line_3', 'Cruise_14-Line_4', 'Cruise_14-Line_6', 'Cruise_14-Line_7', 'sue_shelikof']))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = ['CMI KBNERR: Line 1 (repeated)', 'CMI KBNERR: Line 2 (repeated)', 'CMI KBNERR: Line 3 (repeated)', 'CMI KBNERR: Line 4 (repeated)', 'CMI KBNERR: Line 6 (repeated)', 'CMI KBNERR: Line 7 (repeated)', 'CMI KBNERR: Sue Shelikof']
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
```

## Cruise_00-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_00-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_00-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_01-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_01-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_01-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_01-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_01-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_02-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_02-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_02-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_02-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_02-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_03-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_03-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_03-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_03-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_03-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_05-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_05-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_05-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_05-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_05-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_06-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_06-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_06-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_06-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_06-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_07-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_07-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_07-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_07-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_07-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_08-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_08-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_08-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_08-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_08-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_09-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_09-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_09-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_09-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_09-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_10-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_10-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_10-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_10-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_10-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_11-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_11-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_11-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_11-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_11-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_12-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_12-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_12-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_12-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_12-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_13-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_13-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_13-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_13-Line_6


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_6_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_6_salt.png
---
name: 
---

```
````


+++

## Cruise_13-Line_7


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_7_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_13-Line_7_salt.png
---
name: 
---

```
````


+++

## Cruise_14-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_14-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_14-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_14-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_14-Line_6


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_6_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_6_salt.png
---
name: 
---

```
````


+++

## Cruise_14-Line_7


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_7_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_14-Line_7_salt.png
---
name: 
---

```
````


+++

## Cruise_15-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_15-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_15-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_15-Line_6


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_6_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_6_salt.png
---
name: 
---

```
````


+++

## Cruise_15-Line_7


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_7_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_15-Line_7_salt.png
---
name: 
---

```
````


+++

## Cruise_16-Line_1


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_1_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_1_salt.png
---
name: 
---

```
````


+++

## Cruise_16-Line_2


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_2_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_2_salt.png
---
name: 
---

```
````


+++

## Cruise_16-Line_3


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_3_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_3_salt.png
---
name: 
---

```
````


+++

## Cruise_16-Line_4


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_4_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_4_salt.png
---
name: 
---

```
````


+++

## Cruise_16-Line_6


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_6_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_6_salt.png
---
name: 
---

```
````


+++

## Cruise_16-Line_7


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_7_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Cruise_16-Line_7_salt.png
---
name: 
---

```
````


+++

## Kbay_timeseries


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Kbay_timeseries_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_Kbay_timeseries_salt.png
---
name: 
---

```
````


+++

## sue_shelikof


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_sue_shelikof_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_cmi_kbnerr_ciofs3/ctd_transects_cmi_kbnerr_sue_shelikof_salt.png
---
name: 
---

```
````

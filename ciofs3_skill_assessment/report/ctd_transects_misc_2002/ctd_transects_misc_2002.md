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

(page:ctd_transects_misc_2002-comparison)=
# CTD transects (2002)

* ctd_transects_misc_2002

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_misc_2002.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_misc_2002.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_misc_2002"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join(['Bear_Jul-02', 'Cohen', 'Glacier', 'Peterson_Jul-02', 'PtAdam_jul-02', 'pogibshi_Jul-02']))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = ['Bear Jul 02', 'Cohen', 'Glacier', 'Peterson Jul 02', 'PtAdam Jul 02', 'Pogibshi Jul 02']
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
```

## Bear_Jul-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Bear_Jul-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Bear_Jul-02_salt.png
---
name: 
---

```
````


+++

## Cohen


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Cohen_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Cohen_salt.png
---
name: 
---

```
````


+++

## Glacier


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Glacier_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Glacier_salt.png
---
name: 
---

```
````


+++

## Peterson_Jul-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Peterson_Jul-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_Peterson_Jul-02_salt.png
---
name: 
---

```
````


+++

## PtAdam_jul-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_PtAdam_jul-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_PtAdam_jul-02_salt.png
---
name: 
---

```
````


+++

## pogibshi_Jul-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_pogibshi_Jul-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_misc_2002_ciofs3/ctd_transects_misc_2002_pogibshi_Jul-02_salt.png
---
name: 
---

```
````

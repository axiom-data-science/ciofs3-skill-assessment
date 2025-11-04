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

(page:ctd_transects_otf_kbnerr-comparison)=
# CTD Transect (OTF KBNERR): Repeated from Anchor Point

* ctd_transects_otf_kbnerr

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_otf_kbnerr.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_otf_kbnerr.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_otf_kbnerr"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join(['2003-07-01']))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = ['OTF KBNERR (repeated)']
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
```

## 2003-07-01


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-01_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-01_salt.png
---
name: 
---

```
````


+++

## 2003-07-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-02_salt.png
---
name: 
---

```
````


+++

## 2003-07-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-04_salt.png
---
name: 
---

```
````


+++

## 2003-07-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-05_salt.png
---
name: 
---

```
````


+++

## 2003-07-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-06_salt.png
---
name: 
---

```
````


+++

## 2003-07-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-07_salt.png
---
name: 
---

```
````


+++

## 2003-07-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-08_salt.png
---
name: 
---

```
````


+++

## 2003-07-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-09_salt.png
---
name: 
---

```
````


+++

## 2003-07-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-10_salt.png
---
name: 
---

```
````


+++

## 2003-07-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-11_salt.png
---
name: 
---

```
````


+++

## 2003-07-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-12_salt.png
---
name: 
---

```
````


+++

## 2003-07-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-13_salt.png
---
name: 
---

```
````


+++

## 2003-07-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-14_salt.png
---
name: 
---

```
````


+++

## 2003-07-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-15_salt.png
---
name: 
---

```
````


+++

## 2003-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-16_salt.png
---
name: 
---

```
````


+++

## 2003-07-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-17_salt.png
---
name: 
---

```
````


+++

## 2003-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-18_salt.png
---
name: 
---

```
````


+++

## 2003-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-19_salt.png
---
name: 
---

```
````


+++

## 2003-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-21_salt.png
---
name: 
---

```
````


+++

## 2003-07-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-22_salt.png
---
name: 
---

```
````


+++

## 2003-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-23_salt.png
---
name: 
---

```
````


+++

## 2003-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-24_salt.png
---
name: 
---

```
````


+++

## 2003-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-25_salt.png
---
name: 
---

```
````


+++

## 2003-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-26_salt.png
---
name: 
---

```
````


+++

## 2003-07-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-28_salt.png
---
name: 
---

```
````


+++

## 2003-07-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-29_salt.png
---
name: 
---

```
````


+++

## 2003-07-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2003-07-30_salt.png
---
name: 
---

```
````


+++

## 2004-07-01


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-01_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-01_salt.png
---
name: 
---

```
````


+++

## 2004-07-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-02_salt.png
---
name: 
---

```
````


+++

## 2004-07-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-03_salt.png
---
name: 
---

```
````


+++

## 2004-07-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-04_salt.png
---
name: 
---

```
````


+++

## 2004-07-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-05_salt.png
---
name: 
---

```
````


+++

## 2004-07-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-06_salt.png
---
name: 
---

```
````


+++

## 2004-07-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-07_salt.png
---
name: 
---

```
````


+++

## 2004-07-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-08_salt.png
---
name: 
---

```
````


+++

## 2004-07-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-09_salt.png
---
name: 
---

```
````


+++

## 2004-07-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-10_salt.png
---
name: 
---

```
````


+++

## 2004-07-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-11_salt.png
---
name: 
---

```
````


+++

## 2004-07-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-12_salt.png
---
name: 
---

```
````


+++

## 2004-07-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-13_salt.png
---
name: 
---

```
````


+++

## 2004-07-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-14_salt.png
---
name: 
---

```
````


+++

## 2004-07-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-15_salt.png
---
name: 
---

```
````


+++

## 2004-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-16_salt.png
---
name: 
---

```
````


+++

## 2004-07-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-17_salt.png
---
name: 
---

```
````


+++

## 2004-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-18_salt.png
---
name: 
---

```
````


+++

## 2004-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-19_salt.png
---
name: 
---

```
````


+++

## 2004-07-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-20_salt.png
---
name: 
---

```
````


+++

## 2004-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-21_salt.png
---
name: 
---

```
````


+++

## 2004-07-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-22_salt.png
---
name: 
---

```
````


+++

## 2004-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-23_salt.png
---
name: 
---

```
````


+++

## 2004-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-24_salt.png
---
name: 
---

```
````


+++

## 2004-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-25_salt.png
---
name: 
---

```
````


+++

## 2004-07-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-27_salt.png
---
name: 
---

```
````


+++

## 2004-07-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-28_salt.png
---
name: 
---

```
````


+++

## 2004-07-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-29_salt.png
---
name: 
---

```
````


+++

## 2004-07-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2004-07-30_salt.png
---
name: 
---

```
````


+++

## 2005-07-01


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-01_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-01_salt.png
---
name: 
---

```
````


+++

## 2005-07-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-02_salt.png
---
name: 
---

```
````


+++

## 2005-07-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-03_salt.png
---
name: 
---

```
````


+++

## 2005-07-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-04_salt.png
---
name: 
---

```
````


+++

## 2005-07-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-05_salt.png
---
name: 
---

```
````


+++

## 2005-07-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-06_salt.png
---
name: 
---

```
````


+++

## 2005-07-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-07_salt.png
---
name: 
---

```
````


+++

## 2005-07-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-08_salt.png
---
name: 
---

```
````


+++

## 2005-07-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-09_salt.png
---
name: 
---

```
````


+++

## 2005-07-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-10_salt.png
---
name: 
---

```
````


+++

## 2005-07-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-11_salt.png
---
name: 
---

```
````


+++

## 2005-07-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-12_salt.png
---
name: 
---

```
````


+++

## 2005-07-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-13_salt.png
---
name: 
---

```
````


+++

## 2005-07-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-14_salt.png
---
name: 
---

```
````


+++

## 2005-07-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-15_salt.png
---
name: 
---

```
````


+++

## 2005-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-16_salt.png
---
name: 
---

```
````


+++

## 2005-07-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-17_salt.png
---
name: 
---

```
````


+++

## 2005-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-18_salt.png
---
name: 
---

```
````


+++

## 2005-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-19_salt.png
---
name: 
---

```
````


+++

## 2005-07-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-20_salt.png
---
name: 
---

```
````


+++

## 2005-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-21_salt.png
---
name: 
---

```
````


+++

## 2005-07-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-22_salt.png
---
name: 
---

```
````


+++

## 2005-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-23_salt.png
---
name: 
---

```
````


+++

## 2005-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-24_salt.png
---
name: 
---

```
````


+++

## 2005-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-25_salt.png
---
name: 
---

```
````


+++

## 2005-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-26_salt.png
---
name: 
---

```
````


+++

## 2005-07-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-27_salt.png
---
name: 
---

```
````


+++

## 2005-07-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-28_salt.png
---
name: 
---

```
````


+++

## 2005-07-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-29_salt.png
---
name: 
---

```
````


+++

## 2005-07-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2005-07-30_salt.png
---
name: 
---

```
````


+++

## 2006-07-01


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-01_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-01_salt.png
---
name: 
---

```
````


+++

## 2006-07-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-02_salt.png
---
name: 
---

```
````


+++

## 2006-07-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-03_salt.png
---
name: 
---

```
````


+++

## 2006-07-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-04_salt.png
---
name: 
---

```
````


+++

## 2006-07-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-05_salt.png
---
name: 
---

```
````


+++

## 2006-07-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-06_salt.png
---
name: 
---

```
````


+++

## 2006-07-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-07_salt.png
---
name: 
---

```
````


+++

## 2006-07-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-09_salt.png
---
name: 
---

```
````


+++

## 2006-07-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-10_salt.png
---
name: 
---

```
````


+++

## 2006-07-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-11_salt.png
---
name: 
---

```
````


+++

## 2006-07-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-12_salt.png
---
name: 
---

```
````


+++

## 2006-07-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-13_salt.png
---
name: 
---

```
````


+++

## 2006-07-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-15_salt.png
---
name: 
---

```
````


+++

## 2006-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-16_salt.png
---
name: 
---

```
````


+++

## 2006-07-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-17_salt.png
---
name: 
---

```
````


+++

## 2006-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-18_salt.png
---
name: 
---

```
````


+++

## 2006-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-19_salt.png
---
name: 
---

```
````


+++

## 2006-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-21_salt.png
---
name: 
---

```
````


+++

## 2006-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-23_salt.png
---
name: 
---

```
````


+++

## 2006-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-25_salt.png
---
name: 
---

```
````


+++

## 2006-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-26_salt.png
---
name: 
---

```
````


+++

## 2006-07-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-27_salt.png
---
name: 
---

```
````


+++

## 2006-07-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_otf_kbnerr_ciofs3/ctd_transects_otf_kbnerr_2006-07-28_salt.png
---
name: 
---

```
````

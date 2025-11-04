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

(page:ctd_transects_gwa-comparison)=
# CTD Transects (GWA): Six repeat transects in Cook Inlet

* ctd_transects_gwa

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_gwa.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_gwa.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_gwa"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join(['transect_3-2012-05-02', 'transect_4-2012-05-02', 'transect_6-2012-05-03', 'transect_7-2012-07-30', 'transect_9-2012-02-14', 'transect_AlongBay-2012-08-15']))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = ['GWA: Transect 3 (repeated)', 'GWA: Transect 4 (repeated)', 'GWA: Transect 6 (repeated)', 'GWA: Transect 7 (repeated)', 'GWA: Transect 9 (repeated)', 'GWA: Transect AlongBay (repeated)']
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
```

## transect_3-2012-05-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2012-05-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2012-05-02_salt.png
---
name: 
---

```
````


+++

## transect_3-2012-07-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2012-07-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2012-07-29_salt.png
---
name: 
---

```
````


+++

## transect_3-2012-10-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2012-10-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2012-10-29_salt.png
---
name: 
---

```
````


+++

## transect_3-2013-04-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2013-04-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2013-04-20_salt.png
---
name: 
---

```
````


+++

## transect_3-2013-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2013-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2013-07-19_salt.png
---
name: 
---

```
````


+++

## transect_3-2013-11-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2013-11-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2013-11-08_salt.png
---
name: 
---

```
````


+++

## transect_3-2014-04-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2014-04-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2014-04-11_salt.png
---
name: 
---

```
````


+++

## transect_3-2014-07-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2014-07-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2014-07-22_salt.png
---
name: 
---

```
````


+++

## transect_3-2014-10-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2014-10-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2014-10-13_salt.png
---
name: 
---

```
````


+++

## transect_3-2015-02-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2015-02-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2015-02-22_salt.png
---
name: 
---

```
````


+++

## transect_3-2015-04-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2015-04-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2015-04-12_salt.png
---
name: 
---

```
````


+++

## transect_3-2015-11-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2015-11-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2015-11-04_salt.png
---
name: 
---

```
````


+++

## transect_3-2016-02-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2016-02-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2016-02-14_salt.png
---
name: 
---

```
````


+++

## transect_3-2016-04-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2016-04-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2016-04-11_salt.png
---
name: 
---

```
````


+++

## transect_3-2016-08-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2016-08-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2016-08-29_salt.png
---
name: 
---

```
````


+++

## transect_3-2017-04-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2017-04-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2017-04-19_salt.png
---
name: 
---

```
````


+++

## transect_3-2017-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2017-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2017-07-25_salt.png
---
name: 
---

```
````


+++

## transect_3-2018-06-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2018-06-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2018-06-25_salt.png
---
name: 
---

```
````


+++

## transect_3-2018-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2018-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2018-07-26_salt.png
---
name: 
---

```
````


+++

## transect_3-2018-09-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2018-09-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2018-09-13_salt.png
---
name: 
---

```
````


+++

## transect_3-2019-02-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-02-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-02-08_salt.png
---
name: 
---

```
````


+++

## transect_3-2019-05-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-05-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-05-14_salt.png
---
name: 
---

```
````


+++

## transect_3-2019-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-07-25_salt.png
---
name: 
---

```
````


+++

## transect_3-2019-09-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-09-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2019-09-16_salt.png
---
name: 
---

```
````


+++

## transect_3-2020-07-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2020-07-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2020-07-29_salt.png
---
name: 
---

```
````


+++

## transect_3-2021-04-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2021-04-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2021-04-16_salt.png
---
name: 
---

```
````


+++

## transect_3-2021-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2021-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_3-2021-07-16_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-05-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-05-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-05-02_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-05-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-05-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-05-31_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-06-05_A


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-06-05_A_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-06-05_A_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-06-05_B


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-06-05_B_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-06-05_B_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-07-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-07-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-07-31_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-08-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-08-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-08-15_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-10-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-10-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2012-10-29_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-02-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-02-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-02-12_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-04-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-04-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-04-21_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-06-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-06-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-06-06_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-07-19_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-10-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-10-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2013-10-29_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-02-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-02-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-02-15_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-04-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-04-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-04-11_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-07-21_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-08-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-08-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-08-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-10-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-10-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2014-10-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-02-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-02-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-02-12_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-02-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-02-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-02-24_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-04-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-04-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-04-08_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-08-14_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-09-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-09-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-09-24_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-10-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-10-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-10-19_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-11-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-11-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-11-03_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-11-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-11-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-11-04_salt.png
---
name: 
---

```
````


+++

## transect_4-2015-12-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-12-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2015-12-10_salt.png
---
name: 
---

```
````


+++

## transect_4-2016-02-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-02-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-02-09_salt.png
---
name: 
---

```
````


+++

## transect_4-2016-04-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-04-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-04-11_salt.png
---
name: 
---

```
````


+++

## transect_4-2016-07-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-07-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-07-27_salt.png
---
name: 
---

```
````


+++

## transect_4-2016-10-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-10-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-10-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2016-12-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-12-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2016-12-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2017-04-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2017-04-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2017-04-20_salt.png
---
name: 
---

```
````


+++

## transect_4-2017-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2017-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2017-07-25_salt.png
---
name: 
---

```
````


+++

## transect_4-2017-10-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2017-10-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2017-10-17_salt.png
---
name: 
---

```
````


+++

## transect_4-2018-04-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-04-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-04-23_salt.png
---
name: 
---

```
````


+++

## transect_4-2018-06-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-06-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-06-25_salt.png
---
name: 
---

```
````


+++

## transect_4-2018-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-07-24_salt.png
---
name: 
---

```
````


+++

## transect_4-2018-09-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-09-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2018-09-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2019-02-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-02-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-02-07_salt.png
---
name: 
---

```
````


+++

## transect_4-2019-05-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-05-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-05-14_salt.png
---
name: 
---

```
````


+++

## transect_4-2019-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-07-25_salt.png
---
name: 
---

```
````


+++

## transect_4-2019-09-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-09-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2019-09-16_salt.png
---
name: 
---

```
````


+++

## transect_4-2020-02-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2020-02-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2020-02-14_salt.png
---
name: 
---

```
````


+++

## transect_4-2020-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2020-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2020-07-23_salt.png
---
name: 
---

```
````


+++

## transect_4-2020-09-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2020-09-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2020-09-21_salt.png
---
name: 
---

```
````


+++

## transect_4-2021-02-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-02-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-02-17_salt.png
---
name: 
---

```
````


+++

## transect_4-2021-04-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-04-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-04-16_salt.png
---
name: 
---

```
````


+++

## transect_4-2021-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-07-16_salt.png
---
name: 
---

```
````


+++

## transect_4-2021-09-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-09-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2021-09-17_salt.png
---
name: 
---

```
````


+++

## transect_4-2022-03-01


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2022-03-01_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2022-03-01_salt.png
---
name: 
---

```
````


+++

## transect_4-2022-04-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2022-04-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2022-04-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2022-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2022-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2022-07-23_salt.png
---
name: 
---

```
````


+++

## transect_4-2023-02-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-02-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-02-18_salt.png
---
name: 
---

```
````


+++

## transect_4-2023-05-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-05-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-05-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2023-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-07-25_salt.png
---
name: 
---

```
````


+++

## transect_4-2023-09-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-09-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2023-09-15_salt.png
---
name: 
---

```
````


+++

## transect_4-2024-03-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2024-03-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2024-03-06_salt.png
---
name: 
---

```
````


+++

## transect_4-2024-04-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2024-04-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2024-04-04_salt.png
---
name: 
---

```
````


+++

## transect_4-2024-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2024-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_4-2024-07-19_salt.png
---
name: 
---

```
````


+++

## transect_6-2012-05-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2012-05-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2012-05-03_salt.png
---
name: 
---

```
````


+++

## transect_6-2012-07-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2012-07-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2012-07-30_salt.png
---
name: 
---

```
````


+++

## transect_6-2012-10-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2012-10-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2012-10-28_salt.png
---
name: 
---

```
````


+++

## transect_6-2013-04-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2013-04-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2013-04-19_salt.png
---
name: 
---

```
````


+++

## transect_6-2013-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2013-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2013-07-21_salt.png
---
name: 
---

```
````


+++

## transect_6-2013-11-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2013-11-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2013-11-06_salt.png
---
name: 
---

```
````


+++

## transect_6-2014-04-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2014-04-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2014-04-06_salt.png
---
name: 
---

```
````


+++

## transect_6-2014-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2014-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2014-07-23_salt.png
---
name: 
---

```
````


+++

## transect_6-2014-10-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2014-10-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2014-10-18_salt.png
---
name: 
---

```
````


+++

## transect_6-2015-02-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2015-02-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2015-02-23_salt.png
---
name: 
---

```
````


+++

## transect_6-2015-04-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2015-04-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2015-04-08_salt.png
---
name: 
---

```
````


+++

## transect_6-2015-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2015-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2015-08-14_salt.png
---
name: 
---

```
````


+++

## transect_6-2016-02-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-02-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-02-15_salt.png
---
name: 
---

```
````


+++

## transect_6-2016-04-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-04-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-04-10_salt.png
---
name: 
---

```
````


+++

## transect_6-2016-08-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-08-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-08-31_salt.png
---
name: 
---

```
````


+++

## transect_6-2016-12-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-12-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2016-12-12_salt.png
---
name: 
---

```
````


+++

## transect_6-2017-04-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2017-04-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2017-04-18_salt.png
---
name: 
---

```
````


+++

## transect_6-2017-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2017-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2017-07-26_salt.png
---
name: 
---

```
````


+++

## transect_6-2017-11-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2017-11-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2017-11-02_salt.png
---
name: 
---

```
````


+++

## transect_6-2018-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2018-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2018-07-18_salt.png
---
name: 
---

```
````


+++

## transect_6-2018-09-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2018-09-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2018-09-17_salt.png
---
name: 
---

```
````


+++

## transect_6-2019-02-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2019-02-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2019-02-08_salt.png
---
name: 
---

```
````


+++

## transect_6-2019-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2019-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2019-05-12_salt.png
---
name: 
---

```
````


+++

## transect_6-2019-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2019-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2019-07-25_salt.png
---
name: 
---

```
````


+++

## transect_6-2020-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2020-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2020-07-24_salt.png
---
name: 
---

```
````


+++

## transect_6-2020-09-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2020-09-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2020-09-20_salt.png
---
name: 
---

```
````


+++

## transect_6-2021-02-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-02-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-02-16_salt.png
---
name: 
---

```
````


+++

## transect_6-2021-04-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-04-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-04-14_salt.png
---
name: 
---

```
````


+++

## transect_6-2021-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-07-21_salt.png
---
name: 
---

```
````


+++

## transect_6-2021-10-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-10-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2021-10-05_salt.png
---
name: 
---

```
````


+++

## transect_6-2022-02-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2022-02-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2022-02-28_salt.png
---
name: 
---

```
````


+++

## transect_6-2022-04-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2022-04-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2022-04-12_salt.png
---
name: 
---

```
````


+++

## transect_6-2022-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2022-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2022-07-21_salt.png
---
name: 
---

```
````


+++

## transect_6-2023-03-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-03-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-03-08_salt.png
---
name: 
---

```
````


+++

## transect_6-2023-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-05-12_salt.png
---
name: 
---

```
````


+++

## transect_6-2023-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-07-24_salt.png
---
name: 
---

```
````


+++

## transect_6-2023-09-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-09-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2023-09-13_salt.png
---
name: 
---

```
````


+++

## transect_6-2024-04-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2024-04-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2024-04-03_salt.png
---
name: 
---

```
````


+++

## transect_6-2024-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2024-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_6-2024-07-18_salt.png
---
name: 
---

```
````


+++

## transect_7-2012-07-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2012-07-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2012-07-30_salt.png
---
name: 
---

```
````


+++

## transect_7-2012-10-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2012-10-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2012-10-28_salt.png
---
name: 
---

```
````


+++

## transect_7-2013-04-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2013-04-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2013-04-20_salt.png
---
name: 
---

```
````


+++

## transect_7-2013-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2013-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2013-07-18_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-02-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-02-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-02-17_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-04-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-04-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-04-07_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-07-24_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-10-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-10-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-10-17_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-10-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-10-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2014-10-18_salt.png
---
name: 
---

```
````


+++

## transect_7-2015-02-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2015-02-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2015-02-24_salt.png
---
name: 
---

```
````


+++

## transect_7-2015-04-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2015-04-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2015-04-13_salt.png
---
name: 
---

```
````


+++

## transect_7-2015-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2015-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2015-08-14_salt.png
---
name: 
---

```
````


+++

## transect_7-2016-02-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2016-02-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2016-02-16_salt.png
---
name: 
---

```
````


+++

## transect_7-2016-08-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2016-08-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2016-08-30_salt.png
---
name: 
---

```
````


+++

## transect_7-2016-12-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2016-12-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2016-12-13_salt.png
---
name: 
---

```
````


+++

## transect_7-2017-04-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2017-04-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2017-04-19_salt.png
---
name: 
---

```
````


+++

## transect_7-2017-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2017-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2017-07-26_salt.png
---
name: 
---

```
````


+++

## transect_7-2017-11-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2017-11-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2017-11-02_salt.png
---
name: 
---

```
````


+++

## transect_7-2018-03-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2018-03-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2018-03-27_salt.png
---
name: 
---

```
````


+++

## transect_7-2018-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2018-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2018-07-18_salt.png
---
name: 
---

```
````


+++

## transect_7-2018-09-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2018-09-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2018-09-17_salt.png
---
name: 
---

```
````


+++

## transect_7-2019-02-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-02-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-02-08_salt.png
---
name: 
---

```
````


+++

## transect_7-2019-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-05-12_salt.png
---
name: 
---

```
````


+++

## transect_7-2019-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-07-25_salt.png
---
name: 
---

```
````


+++

## transect_7-2019-09-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-09-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2019-09-19_salt.png
---
name: 
---

```
````


+++

## transect_7-2020-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2020-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2020-07-24_salt.png
---
name: 
---

```
````


+++

## transect_7-2020-09-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2020-09-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2020-09-20_salt.png
---
name: 
---

```
````


+++

## transect_7-2021-02-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-02-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-02-16_salt.png
---
name: 
---

```
````


+++

## transect_7-2021-04-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-04-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-04-14_salt.png
---
name: 
---

```
````


+++

## transect_7-2021-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-07-21_salt.png
---
name: 
---

```
````


+++

## transect_7-2021-10-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-10-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2021-10-05_salt.png
---
name: 
---

```
````


+++

## transect_7-2022-02-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2022-02-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2022-02-28_salt.png
---
name: 
---

```
````


+++

## transect_7-2022-04-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2022-04-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2022-04-12_salt.png
---
name: 
---

```
````


+++

## transect_7-2022-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2022-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2022-07-21_salt.png
---
name: 
---

```
````


+++

## transect_7-2023-03-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-03-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-03-08_salt.png
---
name: 
---

```
````


+++

## transect_7-2023-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-05-12_salt.png
---
name: 
---

```
````


+++

## transect_7-2023-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-07-24_salt.png
---
name: 
---

```
````


+++

## transect_7-2023-09-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-09-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2023-09-13_salt.png
---
name: 
---

```
````


+++

## transect_7-2024-04-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2024-04-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2024-04-03_salt.png
---
name: 
---

```
````


+++

## transect_7-2024-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2024-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_7-2024-07-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-02-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-02-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-02-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-03-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-03-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-03-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-04-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-04-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-04-10_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-04-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-04-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-04-26_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-05-31_A


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-05-31_A_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-05-31_A_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-05-31_B


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-05-31_B_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-05-31_B_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-06-05_A


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-06-05_A_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-06-05_A_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-06-05_B


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-06-05_B_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-06-05_B_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-06-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-06-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-06-27_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-07-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-07-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-07-02_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-07-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-03_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-26_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-08-31_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_A


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_A_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_A_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_B


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_B_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_B_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_C


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_C_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_C_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_D


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_D_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_D_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_E


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_E_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-09-21_E_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-10-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-10-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-10-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-10-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-10-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2012-10-29_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-01-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-01-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-01-04_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-02-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-02-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-02-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-03-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-03-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-03-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-04-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-04-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-04-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-05-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-05-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-05-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-06-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-06-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-06-06_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-06-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-06-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-06-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-06-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-06-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-06-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-07-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-07-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-07-05_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-07-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-07-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-07-09_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-07-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-07-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-07-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-08-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-08-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-08-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-08-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-08-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-08-30_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-09-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-09-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-09-25_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-10-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-10-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-10-29_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-12-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-12-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2013-12-03_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-01-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-01-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-01-09_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-02-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-02-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-02-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-03-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-03-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-03-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-04-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-04-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-04-11_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-05-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-05-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-05-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-06-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-06-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-06-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-07-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-08-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-08-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-08-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-10-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-10-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-10-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-11-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-11-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-11-25_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-12-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-12-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2014-12-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-01-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-01-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-01-16_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-02-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-02-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-02-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-02-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-02-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-02-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-03-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-03-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-03-31_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-04-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-04-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-04-08_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-05-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-05-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-05-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-06-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-06-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-06-26_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-07-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-07-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-07-10_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-07-29


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-07-29_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-07-29_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-08-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-09-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-09-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-09-04_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-09-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-09-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-09-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-10-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-10-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-10-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-11-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-11-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-11-04_salt.png
---
name: 
---

```
````


+++

## transect_9-2015-12-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-12-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2015-12-10_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-01-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-01-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-01-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-02-09


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-02-09_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-02-09_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-04-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-04-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-04-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-05-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-06-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-06-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-06-16_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-07-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-07-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-07-27_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-09-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-09-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-09-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-10-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-10-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-10-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-11-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-11-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-11-10_salt.png
---
name: 
---

```
````


+++

## transect_9-2016-12-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-12-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2016-12-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-01-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-01-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-01-11_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-02-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-02-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-02-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-03-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-03-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-03-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-04-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-04-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-04-20_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-05-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-05-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-05-30_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-06-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-06-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-06-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-07-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-08-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-08-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-08-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-09-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-09-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-09-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-10-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-10-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-10-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-11-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-11-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-11-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2017-12-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-12-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2017-12-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-01-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-01-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-01-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-03-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-03-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-03-02_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-03-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-03-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-03-27_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-04-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-04-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-04-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-05-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-05-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-05-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-06-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-06-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-06-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-07-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-08-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-08-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-08-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-09-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-09-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-09-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-10-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-10-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-10-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-11-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-11-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-11-08_salt.png
---
name: 
---

```
````


+++

## transect_9-2018-12-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-12-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2018-12-06_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-02-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-02-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-02-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-03-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-03-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-03-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-04-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-04-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-04-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-05-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-05-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-05-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-06-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-06-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-06-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-07-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-09-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-09-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-09-16_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-10-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-10-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-10-30_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-11-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-11-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-11-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2019-12-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-12-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2019-12-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-02-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-02-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-02-06_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-03-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-03-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-03-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-06-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-06-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-06-04_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-07-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-08-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-09-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-09-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-09-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-10-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-10-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-10-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2020-12-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-12-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2020-12-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-01-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-01-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-01-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-02-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-02-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-02-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-03-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-03-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-03-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-04-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-04-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-04-16_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-05-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-05-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-05-06_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-06-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-06-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-06-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-07-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-07-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-07-16_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-08-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-08-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-08-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-09-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-09-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-09-17_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-10-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-10-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-10-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-11-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-11-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-11-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2021-12-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-12-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2021-12-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-01-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-01-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-01-31_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-03-01


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-03-01_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-03-01_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-03-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-03-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-03-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-04-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-04-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-04-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-05-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-05-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-05-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-06-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-06-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-06-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-07-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2022-08-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-08-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2022-08-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-01-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-01-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-01-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-02-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-02-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-02-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-03-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-03-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-03-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-04-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-04-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-04-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-05-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-05-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-05-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-06-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-06-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-06-23_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-07-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-07-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-07-25_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-08-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-08-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-08-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-09-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-09-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-09-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-10-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-10-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-10-25_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-11-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-11-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-11-24_salt.png
---
name: 
---

```
````


+++

## transect_9-2023-12-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-12-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2023-12-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-01-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-01-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-01-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-03-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-03-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-03-06_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-04-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-04-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-04-04_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-05-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-05-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-05-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-06-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-06-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-06-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-07-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-07-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-07-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2024-08-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-08-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_9-2024-08-26_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2012-08-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2012-08-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2012-08-15_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-02-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-02-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-02-12_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-02-13_A


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-02-13_A_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-02-13_A_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-02-13_B


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-02-13_B_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-02-13_B_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-06-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-06-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2013-06-06_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2014-03-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2014-03-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2014-03-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2014-05-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2014-05-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2014-05-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2014-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2014-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2014-08-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2015-07-10


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2015-07-10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2015-07-10_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2015-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2015-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2015-08-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2016-01-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-01-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-01-07_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2016-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-05-12_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2016-06-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-06-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-06-16_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2016-07-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-07-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2016-07-27_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-01-11


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-01-11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-01-11_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-02-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-02-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-02-07_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-03-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-03-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-03-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-04-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-04-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-04-20_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-05-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-05-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-05-30_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-06-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-06-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-06-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-07-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-07-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-07-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-07-26_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-08-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-08-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-08-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-09-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-09-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-09-22_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-10-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-10-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-10-20_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-11-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-11-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-11-02_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-11-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-11-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-11-07_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2017-12-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-12-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2017-12-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-01-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-01-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-01-17_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-03-02


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-03-02_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-03-02_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-03-27


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-03-27_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-03-27_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-04-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-04-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-04-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-05-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-05-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-05-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-06-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-06-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-06-22_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-07-18_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-08-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-08-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-08-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-09-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-09-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-09-17_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-10-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-10-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-10-17_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-11-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-11-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-11-08_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2018-12-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-12-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2018-12-06_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-02-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-02-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-02-07_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-03-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-03-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-03-19_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-04-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-04-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-04-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-05-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-05-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-05-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-06-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-06-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-06-19_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-07-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-10-30


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-10-30_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-10-30_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-11-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-11-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-11-15_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2019-12-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-12-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2019-12-12_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-02-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-02-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-02-06_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-03-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-03-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-03-18_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-06-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-06-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-06-04_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-07-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-07-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-07-08_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-07-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-07-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-07-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-08-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-08-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-08-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-09-20


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-09-20_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-09-20_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-10-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-10-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-10-15_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2020-12-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-12-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2020-12-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-01-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-01-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-01-13_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-02-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-02-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-02-16_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-03-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-03-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-03-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-04-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-04-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-04-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-04-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-04-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-04-16_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-05-06


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-05-06_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-05-06_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-06-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-06-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-06-21_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-07-21_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-08-17


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-08-17_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-08-17_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-10-04


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-10-04_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-10-04_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-10-05


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-10-05_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-10-05_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-10-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-10-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-10-21_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-11-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-11-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-11-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2021-12-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-12-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2021-12-18_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-01-31


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-01-31_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-01-31_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-02-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-02-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-02-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-03-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-03-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-03-21_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-04-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-04-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-04-12_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-05-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-05-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-05-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-06-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-06-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-06-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-07-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-07-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-07-21_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2022-08-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-08-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2022-08-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-01-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-01-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-01-18_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-02-16


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-02-16_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-02-16_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-03-08


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-03-08_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-03-08_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-03-28


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-03-28_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-03-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-04-21


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-04-21_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-04-21_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-05-12


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-05-12_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-05-12_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-06-23


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-06-23_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-06-23_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-07-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-07-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-07-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-08-22


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-08-22_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-08-22_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-09-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-09-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-09-13_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-10-25


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-10-25_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-10-25_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-11-24


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-11-24_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-11-24_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2023-12-15


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-12-15_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2023-12-15_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-01-19


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-01-19_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-01-19_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-03-07


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-03-07_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-03-07_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-04-03


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-04-03_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-04-03_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-05-14


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-05-14_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-05-14_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-06-13


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-06-13_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-06-13_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-07-18


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-07-18_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-07-18_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2024-08-26


+++

### Sea Temperature [C]


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-08-26_temp.png
---
name: 
---

```
````


+++

### Salinity


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs3/ctd_transects_gwa_transect_AlongBay-2024-08-26_salt.png
---
name: 
---

```
````

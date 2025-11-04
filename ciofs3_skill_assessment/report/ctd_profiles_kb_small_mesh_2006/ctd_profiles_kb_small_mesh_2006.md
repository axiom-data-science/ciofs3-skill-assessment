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

(page:ctd_profiles_kb_small_mesh_2006-comparison)=
# CTD Profiles (KB small mesh 2006)

* ctd_profiles_kb_small_mesh_2006

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_kb_small_mesh_2006.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_kb_small_mesh_2006.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_kb_small_mesh_2006"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## 1001


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1001_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1001_salt.png
:width: 49%
```

+++

## 1002


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1002_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1002_salt.png
:width: 49%
```

+++

## 1003


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1003_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1003_salt.png
:width: 49%
```

+++

## 1004


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1004_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1004_salt.png
:width: 49%
```

+++

## 1005


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1005_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1005_salt.png
:width: 49%
```

+++

## 1006


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1006_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1006_salt.png
:width: 49%
```

+++

## 1007


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1007_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1007_salt.png
:width: 49%
```

+++

## 1008


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1008_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1008_salt.png
:width: 49%
```

+++

## 1009


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1009_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1009_salt.png
:width: 49%
```

+++

## 1010


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1010_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1010_salt.png
:width: 49%
```

+++

## 1011


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1011_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1011_salt.png
:width: 49%
```

+++

## 1012


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1012_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1012_salt.png
:width: 49%
```

+++

## 1013


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1013_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1013_salt.png
:width: 49%
```

+++

## 1014


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1014_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1014_salt.png
:width: 49%
```

+++

## 1015


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1015_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1015_salt.png
:width: 49%
```

+++

## 1017


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1017_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1017_salt.png
:width: 49%
```

+++

## 1018


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1018_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1018_salt.png
:width: 49%
```

+++

## 1019


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1019_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1019_salt.png
:width: 49%
```

+++

## 1020


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1020_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1020_salt.png
:width: 49%
```

+++

## 1021


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1021_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1021_salt.png
:width: 49%
```

+++

## 1022


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1022_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1022_salt.png
:width: 49%
```

+++

## 1023


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1023_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1023_salt.png
:width: 49%
```

+++

## 1024


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1024_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1024_salt.png
:width: 49%
```

+++

## 1025


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1025_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1025_salt.png
:width: 49%
```

+++

## 1026


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1026_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1026_salt.png
:width: 49%
```

+++

## 1027


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1027_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1027_salt.png
:width: 49%
```

+++

## 1028


+++


```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1028_temp.png
:width: 49%
```

```{image} ctd_profiles_kb_small_mesh_2006_ciofs3/ctd_profiles_kb_small_mesh_2006_1028_salt.png
:width: 49%
```

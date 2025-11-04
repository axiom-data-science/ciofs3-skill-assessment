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

(page:ctd_profiles_emap_2002-comparison)=
# CTD Profiles (EMAP 2002)

* ctd_profiles_emap_2002

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_emap_2002.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_emap_2002.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_emap_2002"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## 10


+++



+++

## 11


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_11_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_11_salt.png
:width: 49%
```

+++

## 12


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_12_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_12_salt.png
:width: 49%
```

+++

## 15


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_15_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_15_salt.png
:width: 49%
```

+++

## 16


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_16_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_16_salt.png
:width: 49%
```

+++

## 17


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_17_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_17_salt.png
:width: 49%
```

+++

## 19


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_19_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_19_salt.png
:width: 49%
```

+++

## 2


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_2_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_2_salt.png
:width: 49%
```

+++

## 20


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_20_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_20_salt.png
:width: 49%
```

+++

## 21


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_21_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_21_salt.png
:width: 49%
```

+++

## 23


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_23_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_23_salt.png
:width: 49%
```

+++

## 24


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_24_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_24_salt.png
:width: 49%
```

+++

## 26


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_26_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_26_salt.png
:width: 49%
```

+++

## 27


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_27_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_27_salt.png
:width: 49%
```

+++

## 28


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_28_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_28_salt.png
:width: 49%
```

+++

## 29


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_29_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_29_salt.png
:width: 49%
```

+++

## 3


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_3_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_3_salt.png
:width: 49%
```

+++

## 30


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_30_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_30_salt.png
:width: 49%
```

+++

## 32


+++



+++

## 34


+++



+++

## 35


+++



+++

## 36


+++



+++

## 38


+++



+++

## 4


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_4_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_4_salt.png
:width: 49%
```

+++

## 40


+++



+++

## 41


+++



+++

## 45


+++



+++

## 46


+++



+++

## 5


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_5_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_5_salt.png
:width: 49%
```

+++

## 50


+++



+++

## 51


+++



+++

## 53


+++



+++

## 54


+++



+++

## 55


+++



+++

## 56


+++



+++

## 58


+++



+++

## 59


+++



+++

## 60


+++



+++

## 61


+++



+++

## 62


+++



+++

## 63


+++



+++

## 64


+++



+++

## 65


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_65_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_65_salt.png
:width: 49%
```

+++

## 67


+++



+++

## 68


+++



+++

## 7


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_7_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_7_salt.png
:width: 49%
```

+++

## 70


+++



+++

## 71


+++



+++

## 72


+++



+++

## 73


+++



+++

## 74


+++



+++

## 75


+++



+++

## 8


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_8_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_8_salt.png
:width: 49%
```

+++

## 9


+++


```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_9_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2002_ciofs3/ctd_profiles_emap_2002_9_salt.png
:width: 49%
```

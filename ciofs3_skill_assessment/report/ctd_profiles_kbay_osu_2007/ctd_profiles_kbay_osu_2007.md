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

(page:ctd_profiles_kbay_osu_2007-comparison)=
# CTD Profiles (Kbay OSU 2007)

* ctd_profiles_kbay_osu_2007

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_kbay_osu_2007.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_kbay_osu_2007.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_kbay_osu_2007"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## 1


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_1_salt.png
:width: 49%
```

+++

## 10


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_10_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_10_salt.png
:width: 49%
```

+++

## 11


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_11_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_11_salt.png
:width: 49%
```

+++

## 12


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_12_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_12_salt.png
:width: 49%
```

+++

## 13


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_13_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_13_salt.png
:width: 49%
```

+++

## 14


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_14_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_14_salt.png
:width: 49%
```

+++

## 15


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_15_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_15_salt.png
:width: 49%
```

+++

## 16


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_16_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_16_salt.png
:width: 49%
```

+++

## 17


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_17_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_17_salt.png
:width: 49%
```

+++

## 18


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_18_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_18_salt.png
:width: 49%
```

+++

## 19


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_19_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_19_salt.png
:width: 49%
```

+++

## 2


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_2_salt.png
:width: 49%
```

+++

## 20


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_20_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_20_salt.png
:width: 49%
```

+++

## 21


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_21_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_21_salt.png
:width: 49%
```

+++

## 22


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_22_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_22_salt.png
:width: 49%
```

+++

## 23


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_23_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_23_salt.png
:width: 49%
```

+++

## 24


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_24_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_24_salt.png
:width: 49%
```

+++

## 25


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_25_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_25_salt.png
:width: 49%
```

+++

## 26


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_26_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_26_salt.png
:width: 49%
```

+++

## 27


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_27_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_27_salt.png
:width: 49%
```

+++

## 28


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_28_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_28_salt.png
:width: 49%
```

+++

## 29


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_29_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_29_salt.png
:width: 49%
```

+++

## 3


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_3_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_3_salt.png
:width: 49%
```

+++

## 30


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_30_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_30_salt.png
:width: 49%
```

+++

## 31


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_31_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_31_salt.png
:width: 49%
```

+++

## 32


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_32_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_32_salt.png
:width: 49%
```

+++

## 33


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_33_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_33_salt.png
:width: 49%
```

+++

## 34


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_34_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_34_salt.png
:width: 49%
```

+++

## 35


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_35_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_35_salt.png
:width: 49%
```

+++

## 36


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_36_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_36_salt.png
:width: 49%
```

+++

## 37


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_37_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_37_salt.png
:width: 49%
```

+++

## 38


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_38_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_38_salt.png
:width: 49%
```

+++

## 39


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_39_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_39_salt.png
:width: 49%
```

+++

## 4


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_4_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_4_salt.png
:width: 49%
```

+++

## 40


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_40_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_40_salt.png
:width: 49%
```

+++

## 41


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_41_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_41_salt.png
:width: 49%
```

+++

## 42


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_42_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_42_salt.png
:width: 49%
```

+++

## 43


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_43_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_43_salt.png
:width: 49%
```

+++

## 44


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_44_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_44_salt.png
:width: 49%
```

+++

## 45


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_45_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_45_salt.png
:width: 49%
```

+++

## 5


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_5_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_5_salt.png
:width: 49%
```

+++

## 6


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_6_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_6_salt.png
:width: 49%
```

+++

## 7


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_7_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_7_salt.png
:width: 49%
```

+++

## 8


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_8_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_8_salt.png
:width: 49%
```

+++

## 9


+++


```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_9_temp.png
:width: 49%
```

```{image} ctd_profiles_kbay_osu_2007_ciofs3/ctd_profiles_kbay_osu_2007_9_salt.png
:width: 49%
```

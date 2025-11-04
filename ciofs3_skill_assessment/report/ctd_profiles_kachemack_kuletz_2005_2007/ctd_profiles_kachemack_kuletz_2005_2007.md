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

(page:ctd_profiles_kachemack_kuletz_2005_2007-comparison)=
# CTD Profiles (Kachemak Kuletz 2005-2007)

* ctd_profiles_kachemack_kuletz_2005_2007

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_kachemack_kuletz_2005_2007.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_kachemack_kuletz_2005_2007.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_kachemack_kuletz_2005_2007"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## 1.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_1_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_1_0_salt.png
:width: 49%
```

+++

## 1.1


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_1_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_1_1_salt.png
:width: 49%
```

+++

## 10.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10_0_salt.png
:width: 49%
```

+++

## 10000.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10000_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10000_0_salt.png
:width: 49%
```

+++

## 10001.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10001_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10001_0_salt.png
:width: 49%
```

+++

## 10002.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10002_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10002_0_salt.png
:width: 49%
```

+++

## 10003.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10003_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10003_0_salt.png
:width: 49%
```

+++

## 10004.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10004_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10004_0_salt.png
:width: 49%
```

+++

## 10005.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10005_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10005_0_salt.png
:width: 49%
```

+++

## 10006.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10006_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10006_0_salt.png
:width: 49%
```

+++

## 10007.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10007_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10007_0_salt.png
:width: 49%
```

+++

## 10008.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10008_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10008_0_salt.png
:width: 49%
```

+++

## 10009.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10009_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10009_0_salt.png
:width: 49%
```

+++

## 10010.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10010_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10010_0_salt.png
:width: 49%
```

+++

## 10011.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10011_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10011_0_salt.png
:width: 49%
```

+++

## 10012.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10012_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10012_0_salt.png
:width: 49%
```

+++

## 10013.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10013_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10013_0_salt.png
:width: 49%
```

+++

## 10014.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10014_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10014_0_salt.png
:width: 49%
```

+++

## 10015.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10015_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10015_0_salt.png
:width: 49%
```

+++

## 10016.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10016_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10016_0_salt.png
:width: 49%
```

+++

## 10017.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10017_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_10017_0_salt.png
:width: 49%
```

+++

## 101.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_101_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_101_0_salt.png
:width: 49%
```

+++

## 103.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_103_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_103_0_salt.png
:width: 49%
```

+++

## 104.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_104_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_104_0_salt.png
:width: 49%
```

+++

## 105.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_105_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_105_0_salt.png
:width: 49%
```

+++

## 107.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_107_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_107_0_salt.png
:width: 49%
```

+++

## 109.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_109_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_109_0_salt.png
:width: 49%
```

+++

## 11.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_11_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_11_0_salt.png
:width: 49%
```

+++

## 111.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_111_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_111_0_salt.png
:width: 49%
```

+++

## 12.1


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_1_salt.png
:width: 49%
```

+++

## 12.2


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_2_salt.png
:width: 49%
```

+++

## 12.3


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_3_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_3_salt.png
:width: 49%
```

+++

## 12.4


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_4_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_4_salt.png
:width: 49%
```

+++

## 12.5


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_5_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_12_5_salt.png
:width: 49%
```

+++

## 2.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_0_salt.png
:width: 49%
```

+++

## 2.02


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_02_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_02_salt.png
:width: 49%
```

+++

## 2.03


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_03_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_03_salt.png
:width: 49%
```

+++

## 2.2


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_2_salt.png
:width: 49%
```

+++

## 2.3


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_3_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_2_3_salt.png
:width: 49%
```

+++

## 202.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_202_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_202_0_salt.png
:width: 49%
```

+++

## 203.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_203_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_203_0_salt.png
:width: 49%
```

+++

## 204.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_204_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_204_0_salt.png
:width: 49%
```

+++

## 205.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_205_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_205_0_salt.png
:width: 49%
```

+++

## 206.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_206_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_206_0_salt.png
:width: 49%
```

+++

## 207.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_207_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_207_0_salt.png
:width: 49%
```

+++

## 209.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_209_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_209_0_salt.png
:width: 49%
```

+++

## 211.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_211_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_211_0_salt.png
:width: 49%
```

+++

## 3.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_0_salt.png
:width: 49%
```

+++

## 3.01


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_01_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_01_salt.png
:width: 49%
```

+++

## 3.02


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_02_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_02_salt.png
:width: 49%
```

+++

## 3.1


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_1_salt.png
:width: 49%
```

+++

## 3.2


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_3_2_salt.png
:width: 49%
```

+++

## 302.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_302_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_302_0_salt.png
:width: 49%
```

+++

## 304.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_304_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_304_0_salt.png
:width: 49%
```

+++

## 305.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_305_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_305_0_salt.png
:width: 49%
```

+++

## 306.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_306_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_306_0_salt.png
:width: 49%
```

+++

## 309.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_309_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_309_0_salt.png
:width: 49%
```

+++

## 311.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_311_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_311_0_salt.png
:width: 49%
```

+++

## 4.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_4_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_4_0_salt.png
:width: 49%
```

+++

## 4.1


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_4_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_4_1_salt.png
:width: 49%
```

+++

## 5.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_5_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_5_0_salt.png
:width: 49%
```

+++

## 6.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_6_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_6_0_salt.png
:width: 49%
```

+++

## 7.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_7_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_7_0_salt.png
:width: 49%
```

+++

## 8.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_8_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_8_0_salt.png
:width: 49%
```

+++

## 9.0


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_9_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs3/ctd_profiles_kachemack_kuletz_2005_2007_9_0_salt.png
:width: 49%
```

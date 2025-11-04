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

(page:ctd_profiles_piatt_speckman_1999-comparison)=
# CTD Profiles (Piatt Speckman)

* ctd_profiles_piatt_speckman_1999

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_piatt_speckman_1999.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_piatt_speckman_1999.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_piatt_speckman_1999"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## 10159900


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159900_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159900_salt.png
:width: 49%
```

+++

## 10159901


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159901_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159901_salt.png
:width: 49%
```

+++

## 10159902


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159902_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159902_salt.png
:width: 49%
```

+++

## 10159903


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159903_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159903_salt.png
:width: 49%
```

+++

## 10159904


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159904_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159904_salt.png
:width: 49%
```

+++

## 10159905


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159905_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159905_salt.png
:width: 49%
```

+++

## 10159907


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159907_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159907_salt.png
:width: 49%
```

+++

## 10159908


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159908_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159908_salt.png
:width: 49%
```

+++

## 10159909


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159909_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159909_salt.png
:width: 49%
```

+++

## 10159910


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159910_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159910_salt.png
:width: 49%
```

+++

## 10159911


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159911_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159911_salt.png
:width: 49%
```

+++

## 10159913


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159913_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159913_salt.png
:width: 49%
```

+++

## 10159914


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159914_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159914_salt.png
:width: 49%
```

+++

## 10159915


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159915_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159915_salt.png
:width: 49%
```

+++

## 10159916


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159916_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_10159916_salt.png
:width: 49%
```

+++

## 9051600


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051600_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051600_salt.png
:width: 49%
```

+++

## 9051601


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051601_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051601_salt.png
:width: 49%
```

+++

## 9051602


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051602_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051602_salt.png
:width: 49%
```

+++

## 9051603


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051603_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051603_salt.png
:width: 49%
```

+++

## 9051604


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051604_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051604_salt.png
:width: 49%
```

+++

## 9051605


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051605_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051605_salt.png
:width: 49%
```

+++

## 9051606


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051606_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051606_salt.png
:width: 49%
```

+++

## 9051607


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051607_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051607_salt.png
:width: 49%
```

+++

## 9051608


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051608_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051608_salt.png
:width: 49%
```

+++

## 9051609


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051609_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051609_salt.png
:width: 49%
```

+++

## 9051610


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051610_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051610_salt.png
:width: 49%
```

+++

## 9051611


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051611_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051611_salt.png
:width: 49%
```

+++

## 9051612


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051612_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051612_salt.png
:width: 49%
```

+++

## 9051613


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051613_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051613_salt.png
:width: 49%
```

+++

## 9051614


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051614_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051614_salt.png
:width: 49%
```

+++

## 9051615


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051615_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051615_salt.png
:width: 49%
```

+++

## 9051616


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051616_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9051616_salt.png
:width: 49%
```

+++

## 9060400


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060400_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060400_salt.png
:width: 49%
```

+++

## 9060401


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060401_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060401_salt.png
:width: 49%
```

+++

## 9060402


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060402_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060402_salt.png
:width: 49%
```

+++

## 9060403


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060403_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060403_salt.png
:width: 49%
```

+++

## 9060404


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060404_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060404_salt.png
:width: 49%
```

+++

## 9060405


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060405_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060405_salt.png
:width: 49%
```

+++

## 9060406


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060406_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060406_salt.png
:width: 49%
```

+++

## 9060407


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060407_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060407_salt.png
:width: 49%
```

+++

## 9060408


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060408_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060408_salt.png
:width: 49%
```

+++

## 9060409


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060409_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060409_salt.png
:width: 49%
```

+++

## 9060410


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060410_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060410_salt.png
:width: 49%
```

+++

## 9060411


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060411_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060411_salt.png
:width: 49%
```

+++

## 9060412


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060412_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060412_salt.png
:width: 49%
```

+++

## 9060413


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060413_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060413_salt.png
:width: 49%
```

+++

## 9060414


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060414_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060414_salt.png
:width: 49%
```

+++

## 9060415


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060415_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060415_salt.png
:width: 49%
```

+++

## 9060415b


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060415b_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9060415b_salt.png
:width: 49%
```

+++

## 9063000


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063000_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063000_salt.png
:width: 49%
```

+++

## 9063001


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063001_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063001_salt.png
:width: 49%
```

+++

## 9063002


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063002_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063002_salt.png
:width: 49%
```

+++

## 9063003


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063003_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063003_salt.png
:width: 49%
```

+++

## 9063004


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063004_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063004_salt.png
:width: 49%
```

+++

## 9063005


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063005_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063005_salt.png
:width: 49%
```

+++

## 9063006


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063006_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063006_salt.png
:width: 49%
```

+++

## 9063007


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063007_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063007_salt.png
:width: 49%
```

+++

## 9063008


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063008_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063008_salt.png
:width: 49%
```

+++

## 9063009


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063009_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063009_salt.png
:width: 49%
```

+++

## 9063010


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063010_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063010_salt.png
:width: 49%
```

+++

## 9063011


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063011_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063011_salt.png
:width: 49%
```

+++

## 9063012


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063012_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063012_salt.png
:width: 49%
```

+++

## 9063013


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063013_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063013_salt.png
:width: 49%
```

+++

## 9063014


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063014_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063014_salt.png
:width: 49%
```

+++

## 9063015


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063015_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9063015_salt.png
:width: 49%
```

+++

## 9072201


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072201_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072201_salt.png
:width: 49%
```

+++

## 9072202


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072202_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072202_salt.png
:width: 49%
```

+++

## 9072203


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072203_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072203_salt.png
:width: 49%
```

+++

## 9072204


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072204_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072204_salt.png
:width: 49%
```

+++

## 9072205


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072205_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072205_salt.png
:width: 49%
```

+++

## 9072206


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072206_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072206_salt.png
:width: 49%
```

+++

## 9072207


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072207_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072207_salt.png
:width: 49%
```

+++

## 9072208


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072208_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072208_salt.png
:width: 49%
```

+++

## 9072209


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072209_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072209_salt.png
:width: 49%
```

+++

## 9072210


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072210_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072210_salt.png
:width: 49%
```

+++

## 9072211


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072211_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072211_salt.png
:width: 49%
```

+++

## 9072212


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072212_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072212_salt.png
:width: 49%
```

+++

## 9072213


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072213_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072213_salt.png
:width: 49%
```

+++

## 9072214


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072214_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9072214_salt.png
:width: 49%
```

+++

## 90729a00


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a00_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a00_salt.png
:width: 49%
```

+++

## 90729a01


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a01_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a01_salt.png
:width: 49%
```

+++

## 90729a02


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a02_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a02_salt.png
:width: 49%
```

+++

## 90729a03


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a03_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a03_salt.png
:width: 49%
```

+++

## 90729a04


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a04_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a04_salt.png
:width: 49%
```

+++

## 90729a05


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a05_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a05_salt.png
:width: 49%
```

+++

## 90729a06


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a06_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a06_salt.png
:width: 49%
```

+++

## 90729a07


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a07_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a07_salt.png
:width: 49%
```

+++

## 90729a08


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a08_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a08_salt.png
:width: 49%
```

+++

## 90729a09


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a09_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a09_salt.png
:width: 49%
```

+++

## 90729a10


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a10_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a10_salt.png
:width: 49%
```

+++

## 90729a11


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a11_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a11_salt.png
:width: 49%
```

+++

## 90729a12


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a12_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a12_salt.png
:width: 49%
```

+++

## 90729a13


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a13_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a13_salt.png
:width: 49%
```

+++

## 90729a14


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a14_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_90729a14_salt.png
:width: 49%
```

+++

## 9082101


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082101_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082101_salt.png
:width: 49%
```

+++

## 9082102


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082102_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082102_salt.png
:width: 49%
```

+++

## 9082103


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082103_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082103_salt.png
:width: 49%
```

+++

## 9082104


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082104_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082104_salt.png
:width: 49%
```

+++

## 9082106


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082106_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082106_salt.png
:width: 49%
```

+++

## 9082107


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082107_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082107_salt.png
:width: 49%
```

+++

## 9082108


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082108_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082108_salt.png
:width: 49%
```

+++

## 9082109


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082109_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082109_salt.png
:width: 49%
```

+++

## 9082110


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082110_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082110_salt.png
:width: 49%
```

+++

## 9082111


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082111_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082111_salt.png
:width: 49%
```

+++

## 9082112


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082112_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082112_salt.png
:width: 49%
```

+++

## 9082113


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082113_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082113_salt.png
:width: 49%
```

+++

## 9082114


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082114_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082114_salt.png
:width: 49%
```

+++

## 9082115


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082115_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082115_salt.png
:width: 49%
```

+++

## 9082116


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082116_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082116_salt.png
:width: 49%
```

+++

## 9082117


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082117_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082117_salt.png
:width: 49%
```

+++

## 9082118


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082118_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082118_salt.png
:width: 49%
```

+++

## 9082119


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082119_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082119_salt.png
:width: 49%
```

+++

## 9082120


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082120_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082120_salt.png
:width: 49%
```

+++

## 9082121


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082121_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082121_salt.png
:width: 49%
```

+++

## 9082122


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082122_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082122_salt.png
:width: 49%
```

+++

## 9082123


+++


```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082123_temp.png
:width: 49%
```

```{image} ctd_profiles_piatt_speckman_1999_ciofs3/ctd_profiles_piatt_speckman_1999_9082123_salt.png
:width: 49%
```

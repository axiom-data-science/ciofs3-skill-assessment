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

(page:ctd_profiles_usgs_boem-comparison)=
# CTD Profiles (USGS BOEM): across Cook Inlet

* ctd_profiles_usgs_boem

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_usgs_boem.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_usgs_boem.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_usgs_boem"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## 2016102001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016102001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016102001_salt.png
:width: 49%
```

+++

## 2016106001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016106001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016106001_salt.png
:width: 49%
```

+++

## 2016120001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016120001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016120001_salt.png
:width: 49%
```

+++

## 2016122201


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016122201_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016122201_salt.png
:width: 49%
```

+++

## 2016123001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016123001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016123001_salt.png
:width: 49%
```

+++

## 2016123002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016123002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016123002_salt.png
:width: 49%
```

+++

## 2016125001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016125001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016125001_salt.png
:width: 49%
```

+++

## 2016126001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016126001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016126001_salt.png
:width: 49%
```

+++

## 2016126002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016126002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016126002_salt.png
:width: 49%
```

+++

## 2016205701


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016205701_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016205701_salt.png
:width: 49%
```

+++

## 2016206001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016206001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016206001_salt.png
:width: 49%
```

+++

## 2016221001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016221001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016221001_salt.png
:width: 49%
```

+++

## 2016223001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016223001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016223001_salt.png
:width: 49%
```

+++

## 2016223002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016223002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016223002_salt.png
:width: 49%
```

+++

## 2016224001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016224001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016224001_salt.png
:width: 49%
```

+++

## 2016225001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016225001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016225001_salt.png
:width: 49%
```

+++

## 2016226001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016226001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2016226001_salt.png
:width: 49%
```

+++

## 2017101001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017101001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017101001_salt.png
:width: 49%
```

+++

## 2017103001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017103001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017103001_salt.png
:width: 49%
```

+++

## 2017120001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017120001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017120001_salt.png
:width: 49%
```

+++

## 2017122001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017122001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017122001_salt.png
:width: 49%
```

+++

## 2017123001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017123001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017123001_salt.png
:width: 49%
```

+++

## 2017124001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017124001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017124001_salt.png
:width: 49%
```

+++

## 2017125001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017125001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017125001_salt.png
:width: 49%
```

+++

## 2017125002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017125002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017125002_salt.png
:width: 49%
```

+++

## 2017201001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017201001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017201001_salt.png
:width: 49%
```

+++

## 2017204001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017204001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017204001_salt.png
:width: 49%
```

+++

## 2017205001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017205001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017205001_salt.png
:width: 49%
```

+++

## 2017206001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017206001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017206001_salt.png
:width: 49%
```

+++

## 2017207001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017207001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017207001_salt.png
:width: 49%
```

+++

## 2017212001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017212001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017212001_salt.png
:width: 49%
```

+++

## 2017214001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017214001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017214001_salt.png
:width: 49%
```

+++

## 2017220001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017220001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017220001_salt.png
:width: 49%
```

+++

## 2017223001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017223001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017223001_salt.png
:width: 49%
```

+++

## 2017224001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017224001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017224001_salt.png
:width: 49%
```

+++

## 2017225001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017225001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2017225001_salt.png
:width: 49%
```

+++

## 2018104001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018104001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018104001_salt.png
:width: 49%
```

+++

## 2018120001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018120001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018120001_salt.png
:width: 49%
```

+++

## 2018121001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018121001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018121001_salt.png
:width: 49%
```

+++

## 2018122001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018122001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018122001_salt.png
:width: 49%
```

+++

## 2018123001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018123001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018123001_salt.png
:width: 49%
```

+++

## 2018124001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018124001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018124001_salt.png
:width: 49%
```

+++

## 2018125001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018125001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018125001_salt.png
:width: 49%
```

+++

## 2018126001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018126001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018126001_salt.png
:width: 49%
```

+++

## 2018203001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018203001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018203001_salt.png
:width: 49%
```

+++

## 2018203002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018203002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018203002_salt.png
:width: 49%
```

+++

## 2018205001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018205001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018205001_salt.png
:width: 49%
```

+++

## 2018208001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018208001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018208001_salt.png
:width: 49%
```

+++

## 2018214002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018214002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018214002_salt.png
:width: 49%
```

+++

## 2018221001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018221001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018221001_salt.png
:width: 49%
```

+++

## 2018223001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018223001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018223001_salt.png
:width: 49%
```

+++

## 2018223002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018223002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018223002_salt.png
:width: 49%
```

+++

## 2018225001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018225001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2018225001_salt.png
:width: 49%
```

+++

## 2019106001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019106001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019106001_salt.png
:width: 49%
```

+++

## 2019121001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019121001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019121001_salt.png
:width: 49%
```

+++

## 2019122001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019122001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019122001_salt.png
:width: 49%
```

+++

## 2019123001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019123001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019123001_salt.png
:width: 49%
```

+++

## 2019125001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019125001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019125001_salt.png
:width: 49%
```

+++

## 2019126001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019126001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019126001_salt.png
:width: 49%
```

+++

## 2019205001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019205001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019205001_salt.png
:width: 49%
```

+++

## 2019210001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019210001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019210001_salt.png
:width: 49%
```

+++

## 2019221001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019221001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019221001_salt.png
:width: 49%
```

+++

## 2019223001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019223001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019223001_salt.png
:width: 49%
```

+++

## 2019223002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019223002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019223002_salt.png
:width: 49%
```

+++

## 2019226001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019226001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2019226001_salt.png
:width: 49%
```

+++

## 2021105001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021105001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021105001_salt.png
:width: 49%
```

+++

## 2021122001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021122001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021122001_salt.png
:width: 49%
```

+++

## 2021123001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021123001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021123001_salt.png
:width: 49%
```

+++

## 2021124001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021124001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021124001_salt.png
:width: 49%
```

+++

## 2021125001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021125001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021125001_salt.png
:width: 49%
```

+++

## 2021126001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021126001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021126001_salt.png
:width: 49%
```

+++

## 2021205001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021205001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021205001_salt.png
:width: 49%
```

+++

## 2021210001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021210001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021210001_salt.png
:width: 49%
```

+++

## 2021221001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021221001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021221001_salt.png
:width: 49%
```

+++

## 2021223001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021223001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021223001_salt.png
:width: 49%
```

+++

## 2021223002


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021223002_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021223002_salt.png
:width: 49%
```

+++

## 2021224001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021224001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021224001_salt.png
:width: 49%
```

+++

## 2021226001


+++


```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021226001_temp.png
:width: 49%
```

```{image} ctd_profiles_usgs_boem_ciofs3/ctd_profiles_usgs_boem_2021226001_salt.png
:width: 49%
```

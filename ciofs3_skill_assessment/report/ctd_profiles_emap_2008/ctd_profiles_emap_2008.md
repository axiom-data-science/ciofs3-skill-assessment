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

(page:ctd_profiles_emap_2008-comparison)=
# CTD Profiles (EMAP 2008)

* ctd_profiles_emap_2008

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_emap_2008.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_emap_2008.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_emap_2008"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## AKCI08-001


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-001_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-001_salt.png
:width: 49%
```

+++

## AKCI08-002


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-002_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-002_salt.png
:width: 49%
```

+++

## AKCI08-003


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-003_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-003_salt.png
:width: 49%
```

+++

## AKCI08-004


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-004_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-004_salt.png
:width: 49%
```

+++

## AKCI08-005


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-005_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-005_salt.png
:width: 49%
```

+++

## AKCI08-007


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-007_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-007_salt.png
:width: 49%
```

+++

## AKCI08-008


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-008_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-008_salt.png
:width: 49%
```

+++

## AKCI08-009


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-009_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-009_salt.png
:width: 49%
```

+++

## AKCI08-011


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-011_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-011_salt.png
:width: 49%
```

+++

## AKCI08-012


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-012_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-012_salt.png
:width: 49%
```

+++

## AKCI08-013


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-013_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-013_salt.png
:width: 49%
```

+++

## AKCI08-015


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-015_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-015_salt.png
:width: 49%
```

+++

## AKCI08-016


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-016_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-016_salt.png
:width: 49%
```

+++

## AKCI08-017


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-017_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-017_salt.png
:width: 49%
```

+++

## AKCI08-018


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-018_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-018_salt.png
:width: 49%
```

+++

## AKCI08-021


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-021_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-021_salt.png
:width: 49%
```

+++

## AKCI08-023


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-023_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-023_salt.png
:width: 49%
```

+++

## AKCI08-024


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-024_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-024_salt.png
:width: 49%
```

+++

## AKCI08-026


+++



+++

## AKCI08-027


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-027_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-027_salt.png
:width: 49%
```

+++

## AKCI08-028


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-028_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-028_salt.png
:width: 49%
```

+++

## AKCI08-029


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-029_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-029_salt.png
:width: 49%
```

+++

## AKCI08-031


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-031_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-031_salt.png
:width: 49%
```

+++

## AKCI08-032


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-032_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-032_salt.png
:width: 49%
```

+++

## AKCI08-033


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-033_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-033_salt.png
:width: 49%
```

+++

## AKCI08-035


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-035_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-035_salt.png
:width: 49%
```

+++

## AKCI08-037A


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-037A_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-037A_salt.png
:width: 49%
```

+++

## AKCI08-037B


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-037B_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-037B_salt.png
:width: 49%
```

+++

## AKCI08-039


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-039_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-039_salt.png
:width: 49%
```

+++

## AKCI08-040


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-040_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-040_salt.png
:width: 49%
```

+++

## AKCI08-041


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-041_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-041_salt.png
:width: 49%
```

+++

## AKCI08-042


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-042_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-042_salt.png
:width: 49%
```

+++

## AKCI08-043


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-043_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-043_salt.png
:width: 49%
```

+++

## AKCI08-044


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-044_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-044_salt.png
:width: 49%
```

+++

## AKCI08-045


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-045_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-045_salt.png
:width: 49%
```

+++

## AKCI08-047


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-047_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-047_salt.png
:width: 49%
```

+++

## AKCI08-048


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-048_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-048_salt.png
:width: 49%
```

+++

## AKCI08-049


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-049_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-049_salt.png
:width: 49%
```

+++

## AKCI08-050


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-050_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-050_salt.png
:width: 49%
```

+++

## AKCI08-051


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-051_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-051_salt.png
:width: 49%
```

+++

## AKCI08-052


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-052_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-052_salt.png
:width: 49%
```

+++

## AKCI08-054


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-054_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-054_salt.png
:width: 49%
```

+++

## AKCI08-055


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-055_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-055_salt.png
:width: 49%
```

+++

## AKCI08-056


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-056_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-056_salt.png
:width: 49%
```

+++

## AKCI08-057


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-057_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-057_salt.png
:width: 49%
```

+++

## AKCI08-058


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-058_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-058_salt.png
:width: 49%
```

+++

## AKCI08-059


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-059_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-059_salt.png
:width: 49%
```

+++

## AKCI08-060


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-060_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-060_salt.png
:width: 49%
```

+++

## AKCI08-061


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-061_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-061_salt.png
:width: 49%
```

+++

## AKCI08-063


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-063_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-063_salt.png
:width: 49%
```

+++

## AKCI08-065


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-065_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-065_salt.png
:width: 49%
```

+++

## AKCI08-066


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-066_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-066_salt.png
:width: 49%
```

+++

## AKCI08-067


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-067_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-067_salt.png
:width: 49%
```

+++

## AKCI08-069


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-069_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-069_salt.png
:width: 49%
```

+++

## AKCI08-070


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-070_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-070_salt.png
:width: 49%
```

+++

## AKCI08-071


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-071_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-071_salt.png
:width: 49%
```

+++

## AKCI08-072


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-072_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-072_salt.png
:width: 49%
```

+++

## AKCI08-073


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-073_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-073_salt.png
:width: 49%
```

+++

## AKCI08-074


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-074_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-074_salt.png
:width: 49%
```

+++

## AKCI08-076


+++



+++

## AKCI08-079


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-079_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-079_salt.png
:width: 49%
```

+++

## AKCI08-080


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-080_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-080_salt.png
:width: 49%
```

+++

## AKCI08-081


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-081_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-081_salt.png
:width: 49%
```

+++

## AKCI08-083


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-083_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-083_salt.png
:width: 49%
```

+++

## AKCI08-084


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-084_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-084_salt.png
:width: 49%
```

+++

## AKCI08-086


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-086_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-086_salt.png
:width: 49%
```

+++

## AKCI08-087


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-087_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-087_salt.png
:width: 49%
```

+++

## AKCI08-088


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-088_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_AKCI08-088_salt.png
:width: 49%
```

+++

## KB01


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB01_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB01_salt.png
:width: 49%
```

+++

## KB02


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB02_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB02_salt.png
:width: 49%
```

+++

## KB03


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB03_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB03_salt.png
:width: 49%
```

+++

## KB04


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB04_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB04_salt.png
:width: 49%
```

+++

## KB05


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB05_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KB05_salt.png
:width: 49%
```

+++

## KRM


+++


```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KRM_temp.png
:width: 49%
```

```{image} ctd_profiles_emap_2008_ciofs3/ctd_profiles_emap_2008_KRM_salt.png
:width: 49%
```

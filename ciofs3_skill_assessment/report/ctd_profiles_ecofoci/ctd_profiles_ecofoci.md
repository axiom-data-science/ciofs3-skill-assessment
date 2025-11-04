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

(page:ctd_profiles_ecofoci-comparison)=
# CTD Profiles (EcoFOCI): Shelikof Strait

* ctd_profiles_ecofoci

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_ecofoci.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_ecofoci.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_ecofoci"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## dy0808c001


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c001_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c001_salt.png
:width: 49%
```

+++

## dy0808c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c002_salt.png
:width: 49%
```

+++

## dy0808c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c003_salt.png
:width: 49%
```

+++

## dy0808c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c004_salt.png
:width: 49%
```

+++

## dy0808c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c005_salt.png
:width: 49%
```

+++

## dy0808c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c006_salt.png
:width: 49%
```

+++

## dy0808c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c007_salt.png
:width: 49%
```

+++

## dy0808c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c008_salt.png
:width: 49%
```

+++

## dy0808c009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c009_salt.png
:width: 49%
```

+++

## dy0808c010


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c010_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c010_salt.png
:width: 49%
```

+++

## dy0808c011


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c011_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c011_salt.png
:width: 49%
```

+++

## dy0808c012


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c012_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c012_salt.png
:width: 49%
```

+++

## dy0808c013


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c013_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy0808c013_salt.png
:width: 49%
```

+++

## dy1204c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c002_salt.png
:width: 49%
```

+++

## dy1204c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c003_salt.png
:width: 49%
```

+++

## dy1204c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c004_salt.png
:width: 49%
```

+++

## dy1204c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c005_salt.png
:width: 49%
```

+++

## dy1204c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c006_salt.png
:width: 49%
```

+++

## dy1204c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c007_salt.png
:width: 49%
```

+++

## dy1204c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_dy1204c008_salt.png
:width: 49%
```

+++

## gp0101c067


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0101c067_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0101c067_salt.png
:width: 49%
```

+++

## gp0101c068


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0101c068_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0101c068_salt.png
:width: 49%
```

+++

## gp0101c069


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0101c069_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0101c069_salt.png
:width: 49%
```

+++

## gp0201c075


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0201c075_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0201c075_salt.png
:width: 49%
```

+++

## gp0201c076


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0201c076_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0201c076_salt.png
:width: 49%
```

+++

## gp0201c077


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0201c077_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_gp0201c077_salt.png
:width: 49%
```

+++

## mf0008c001


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0008c001_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0008c001_salt.png
:width: 49%
```

+++

## mf0008c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0008c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0008c002_salt.png
:width: 49%
```

+++

## mf0008c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0008c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0008c003_salt.png
:width: 49%
```

+++

## mf0105004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105004_salt.png
:width: 49%
```

+++

## mf0105005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105005_salt.png
:width: 49%
```

+++

## mf0105006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105006_salt.png
:width: 49%
```

+++

## mf0105007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105007_salt.png
:width: 49%
```

+++

## mf0105008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105008_salt.png
:width: 49%
```

+++

## mf0105009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0105009_salt.png
:width: 49%
```

+++

## mf0201c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c005_salt.png
:width: 49%
```

+++

## mf0201c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c006_salt.png
:width: 49%
```

+++

## mf0201c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c007_salt.png
:width: 49%
```

+++

## mf0201c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c008_salt.png
:width: 49%
```

+++

## mf0201c009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c009_salt.png
:width: 49%
```

+++

## mf0201c010


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c010_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c010_salt.png
:width: 49%
```

+++

## mf0201c011


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c011_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0201c011_salt.png
:width: 49%
```

+++

## mf0207c001


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c001_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c001_salt.png
:width: 49%
```

+++

## mf0207c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c002_salt.png
:width: 49%
```

+++

## mf0207c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c003_salt.png
:width: 49%
```

+++

## mf0207c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c004_salt.png
:width: 49%
```

+++

## mf0207c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c005_salt.png
:width: 49%
```

+++

## mf0207c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0207c006_salt.png
:width: 49%
```

+++

## mf0303c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0303c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0303c002_salt.png
:width: 49%
```

+++

## mf0309bc013


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc013_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc013_salt.png
:width: 49%
```

+++

## mf0309bc014


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc014_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc014_salt.png
:width: 49%
```

+++

## mf0309bc015


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc015_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc015_salt.png
:width: 49%
```

+++

## mf0309bc016


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc016_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc016_salt.png
:width: 49%
```

+++

## mf0309bc017


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc017_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc017_salt.png
:width: 49%
```

+++

## mf0309bc018


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc018_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc018_salt.png
:width: 49%
```

+++

## mf0309bc019


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc019_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0309bc019_salt.png
:width: 49%
```

+++

## mf0312c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c004_salt.png
:width: 49%
```

+++

## mf0312c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c005_salt.png
:width: 49%
```

+++

## mf0312c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c006_salt.png
:width: 49%
```

+++

## mf0312c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c007_salt.png
:width: 49%
```

+++

## mf0312c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c008_salt.png
:width: 49%
```

+++

## mf0312c009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c009_salt.png
:width: 49%
```

+++

## mf0312c010


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c010_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c010_salt.png
:width: 49%
```

+++

## mf0312c011


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c011_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c011_salt.png
:width: 49%
```

+++

## mf0312c012


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c012_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0312c012_salt.png
:width: 49%
```

+++

## mf0404c025


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c025_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c025_salt.png
:width: 49%
```

+++

## mf0404c026


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c026_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c026_salt.png
:width: 49%
```

+++

## mf0404c027


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c027_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c027_salt.png
:width: 49%
```

+++

## mf0404c029


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c029_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c029_salt.png
:width: 49%
```

+++

## mf0404c030


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c030_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c030_salt.png
:width: 49%
```

+++

## mf0404c031


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c031_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c031_salt.png
:width: 49%
```

+++

## mf0404c032


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c032_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c032_salt.png
:width: 49%
```

+++

## mf0404c033


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c033_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c033_salt.png
:width: 49%
```

+++

## mf0404c034


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c034_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c034_salt.png
:width: 49%
```

+++

## mf0404c035


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c035_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0404c035_salt.png
:width: 49%
```

+++

## mf0405bc001


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0405bc001_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0405bc001_salt.png
:width: 49%
```

+++

## mf0407c001


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c001_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c001_salt.png
:width: 49%
```

+++

## mf0407c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c002_salt.png
:width: 49%
```

+++

## mf0407c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c003_salt.png
:width: 49%
```

+++

## mf0407c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c004_salt.png
:width: 49%
```

+++

## mf0407c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c005_salt.png
:width: 49%
```

+++

## mf0407c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0407c006_salt.png
:width: 49%
```

+++

## mf0504c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c003_salt.png
:width: 49%
```

+++

## mf0504c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c004_salt.png
:width: 49%
```

+++

## mf0504c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c005_salt.png
:width: 49%
```

+++

## mf0504c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c006_salt.png
:width: 49%
```

+++

## mf0504c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c007_salt.png
:width: 49%
```

+++

## mf0504c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c008_salt.png
:width: 49%
```

+++

## mf0504c009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c009_salt.png
:width: 49%
```

+++

## mf0504c010


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c010_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c010_salt.png
:width: 49%
```

+++

## mf0504c011


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c011_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c011_salt.png
:width: 49%
```

+++

## mf0504c012


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c012_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0504c012_salt.png
:width: 49%
```

+++

## mf0508c002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c002_salt.png
:width: 49%
```

+++

## mf0508c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c003_salt.png
:width: 49%
```

+++

## mf0508c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c004_salt.png
:width: 49%
```

+++

## mf0508c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c005_salt.png
:width: 49%
```

+++

## mf0508c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c006_salt.png
:width: 49%
```

+++

## mf0508c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0508c007_salt.png
:width: 49%
```

+++

## mf0602c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c003_salt.png
:width: 49%
```

+++

## mf0602c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c004_salt.png
:width: 49%
```

+++

## mf0602c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c005_salt.png
:width: 49%
```

+++

## mf0602c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c006_salt.png
:width: 49%
```

+++

## mf0602c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c008_salt.png
:width: 49%
```

+++

## mf0602c009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c009_salt.png
:width: 49%
```

+++

## mf0602c010


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c010_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c010_salt.png
:width: 49%
```

+++

## mf0602c011


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c011_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c011_salt.png
:width: 49%
```

+++

## mf0602c012


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c012_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0602c012_salt.png
:width: 49%
```

+++

## mf0702c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c003_salt.png
:width: 49%
```

+++

## mf0702c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c004_salt.png
:width: 49%
```

+++

## mf0702c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c005_salt.png
:width: 49%
```

+++

## mf0702c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c006_salt.png
:width: 49%
```

+++

## mf0702c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c007_salt.png
:width: 49%
```

+++

## mf0702c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c008_salt.png
:width: 49%
```

+++

## mf0702c009


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c009_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0702c009_salt.png
:width: 49%
```

+++

## mf0708c003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c003_salt.png
:width: 49%
```

+++

## mf0708c004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c004_salt.png
:width: 49%
```

+++

## mf0708c005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c005_salt.png
:width: 49%
```

+++

## mf0708c006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c006_salt.png
:width: 49%
```

+++

## mf0708c007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c007_salt.png
:width: 49%
```

+++

## mf0708c008


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c008_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0708c008_salt.png
:width: 49%
```

+++

## mf0802bc036


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc036_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc036_salt.png
:width: 49%
```

+++

## mf0802bc037


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc037_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc037_salt.png
:width: 49%
```

+++

## mf0802bc038


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc038_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc038_salt.png
:width: 49%
```

+++

## mf0802bc039


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc039_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc039_salt.png
:width: 49%
```

+++

## mf0802bc040


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc040_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc040_salt.png
:width: 49%
```

+++

## mf0802bc041


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc041_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_mf0802bc041_salt.png
:width: 49%
```

+++

## rb0103a002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_rb0103a002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_rb0103a002_salt.png
:width: 49%
```

+++

## rb0103a004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_rb0103a004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_rb0103a004_salt.png
:width: 49%
```

+++

## w9905bc001


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc001_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc001_salt.png
:width: 49%
```

+++

## w9905bc002


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc002_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc002_salt.png
:width: 49%
```

+++

## w9905bc003


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc003_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc003_salt.png
:width: 49%
```

+++

## w9905bc004


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc004_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc004_salt.png
:width: 49%
```

+++

## w9905bc005


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc005_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc005_salt.png
:width: 49%
```

+++

## w9905bc006


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc006_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc006_salt.png
:width: 49%
```

+++

## w9905bc007


+++


```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc007_temp.png
:width: 49%
```

```{image} ctd_profiles_ecofoci_ciofs3/ctd_profiles_ecofoci_w9905bc007_salt.png
:width: 49%
```

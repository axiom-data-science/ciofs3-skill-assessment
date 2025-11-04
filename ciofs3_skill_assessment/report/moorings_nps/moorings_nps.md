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

# Moorings (NPS): across Alaska

* moorings_nps

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_nps.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_nps.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_nps"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## aguchik-island-ak-tide-station-9


+++

### Sea surface height: mean subtracted

+++



````{div} full-width                
```{figure} moorings_nps_ciofs3/moorings_nps_aguchik-island-ak-tide-station-9_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++



````{div} full-width                
```{figure} moorings_nps_ciofs3/moorings_nps_aguchik-island-ak-tide-station-9_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

## chinitna-bay-ak-tide-station-945


+++

### Sea surface height: mean subtracted

+++



````{div} full-width                
```{figure} moorings_nps_ciofs3/moorings_nps_chinitna-bay-ak-tide-station-945_ssh_subtract-mean.png
---
name: 
---

```
````

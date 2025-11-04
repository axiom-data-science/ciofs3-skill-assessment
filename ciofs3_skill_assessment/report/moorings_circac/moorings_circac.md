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

# Mooring (CIRCAC): Central Cook Inlet Mooring

* moorings_circac

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_circac.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_circac.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_circac"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## moorings_circac


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_circac_ciofs3/moorings_circac_moorings_circac_salt_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: 

+++



````{div} full-width                
```{figure} moorings_circac_ciofs3/moorings_circac_moorings_circac_salt.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_circac_ciofs3/moorings_circac_moorings_circac_temp_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++



````{div} full-width                
```{figure} moorings_circac_ciofs3/moorings_circac_moorings_circac_temp.png
---
name: 
---

```
````

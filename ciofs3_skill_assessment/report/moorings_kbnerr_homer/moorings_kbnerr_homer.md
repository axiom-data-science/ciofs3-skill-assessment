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

# Moorings (KBNERR): Kachemak Bay, Homer stations

* moorings_kbnerr_homer

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_kbnerr_homer.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_kbnerr_homer.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_kbnerr_homer"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## nerrs_kach3wq


+++

### Sea water salinity: 

+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kach3wq_salt_mean.png
---
name: 
---

```
````


+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_salt_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted

+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kach3wq_temp_mean.png
---
name: 
---

```
````


+++

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kach3wq_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## nerrs_kachdwq


+++

### Sea water salinity: 

+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_salt_mean.png
---
name: 
---

```
````


+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_salt_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted

+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2007-01-01_2008-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2008-01-01_2009-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2009-01-01_2010-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2010-01-01_2011-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2011-01-01_2012-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2009-01-01_2010-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2010-01-01_2011-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2011-01-01_2012-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_temp_mean.png
---
name: 
---

```
````


+++

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs3/moorings_kbnerr_homer_nerrs_kachdwq_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

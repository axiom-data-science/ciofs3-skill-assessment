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

# Moorings (UAF): Kodiak Island, Peterson Bay

* moorings_uaf

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_uaf.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_uaf.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_uaf"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## peterson-bay-ak-gnss-r


+++

### Sea surface height: mean subtracted

+++

##### 2017



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 2017



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_peterson-bay-ak-gnss-r_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

## uaf_ocean_acidification_resea_ko


+++

### Sea water salinity: 

+++

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2015-01-01_2016-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_uaf_uaf_ocean_acidification_resea_ko_salt_mean.png
---
name: 
---

```
````


+++

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_uaf_uaf_ocean_acidification_resea_ko_temp_mean.png
---
name: 
---

```
````


+++

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_uaf_ciofs3/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

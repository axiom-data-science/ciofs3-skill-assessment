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

# Moorings (KBNERR): Historical, Kachemak Bay

* moorings_kbnerr_historical

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_kbnerr_historical.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_kbnerr_historical.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_kbnerr_historical"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## kacbcwq


+++

### Sea water salinity: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacbcwq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacbcwq_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## kacdlwq


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacdlwq_salt_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacdlwq_salt.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacdlwq_temp_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacdlwq_temp.png
---
name: 
---

```
````


+++

## kachowq


+++

### Sea water salinity: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kachowq_salt_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kachowq_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## kacpgwq


+++

### Sea water salinity: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacpgwq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacpgwq_temp_2002-01-01_2003-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacpgwq_temp_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacpgwq_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## kacsewq


+++

### Sea water salinity: 

+++

##### 2001



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_salt_2001-01-01_2002-01-01.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_salt_2002-01-01_2003-01-01.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered

+++

##### 2001



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_salt_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_salt_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_kacsewq_salt_mean.png
---
name: 
---

```
````


+++

##### 2001



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_salt_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_salt_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 2001



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_temp_2001-01-01_2002-01-01.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_temp_2002-01-01_2003-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 2001



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_temp_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_temp_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_kbnerr_historical_kacsewq_temp_mean.png
---
name: 
---

```
````


+++

##### 2001



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs3/moorings_kbnerr_historical_kacsewq_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

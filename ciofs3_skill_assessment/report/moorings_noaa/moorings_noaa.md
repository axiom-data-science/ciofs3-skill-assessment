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

# Moorings (NOAA): across Cook Inlet

* moorings_noaa

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_noaa.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_noaa.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_noaa"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
dd.hvplot(**map) * ddlabels.hvplot(**maplabels)
```

## noaa_nos_co_ops_9455500


+++

### Sea surface height: mean subtracted

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_1999-01-01_2000-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2000-01-01_2001-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2001-01-01_2002-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2002-01-01_2003-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2003-01-01_2004-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2007-01-01_2008-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2008-01-01_2009-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2009-01-01_2010-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2010-01-01_2011-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2011-01-01_2012-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2009-01-01_2010-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2010-01-01_2011-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2011-01-01_2012-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455500_temp_mean.png
---
name: 
---

```
````


+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455500_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## noaa_nos_co_ops_9455595


+++

### Sea surface height: mean subtracted

+++

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455595_ssh_2008-01-01_2009-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455595_ssh_2009-01-01_2010-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455595_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455595_ssh_2009-01-01_2010-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

## noaa_nos_co_ops_9455920


+++

### Sea surface height: mean subtracted

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_1999-01-01_2000-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2000-01-01_2001-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2001-01-01_2002-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2002-01-01_2003-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2003-01-01_2004-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2007-01-01_2008-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2008-01-01_2009-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2009-01-01_2010-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2010-01-01_2011-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2011-01-01_2012-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2009-01-01_2010-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2010-01-01_2011-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2011-01-01_2012-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9455920_temp_mean.png
---
name: 
---

```
````


+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9455920_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## noaa_nos_co_ops_9457292


+++

### Sea surface height: mean subtracted

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_1999-01-01_2000-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2000-01-01_2001-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2001-01-01_2002-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2002-01-01_2003-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2003-01-01_2004-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2007-01-01_2008-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2008-01-01_2009-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2009-01-01_2010-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2010-01-01_2011-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2011-01-01_2012-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_1999-01-01_2000-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2000-01-01_2001-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2001-01-01_2002-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2002-01-01_2003-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2009-01-01_2010-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2010-01-01_2011-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2011-01-01_2012-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_1999-01-01_2000-01-01.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2000-01-01_2001-01-01.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2001-01-01_2002-01-01.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2002-01-01_2003-01-01.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_1999-01-01_2000-01-01_subtidal.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2000-01-01_2001-01-01_subtidal.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2001-01-01_2002-01-01_subtidal.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2002-01-01_2003-01-01_subtidal.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9457292_temp_mean.png
---
name: 
---

```
````


+++

##### 1999



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_1999-01-01_2000-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2000



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2000-01-01_2001-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2001



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2001-01-01_2002-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2002



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2002-01-01_2003-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2003



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457292_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## noaa_nos_co_ops_9457804


+++

### Sea surface height: mean subtracted

+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2007-01-01_2008-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2008-01-01_2009-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2009-01-01_2010-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2010-01-01_2011-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2011-01-01_2012-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2018-01-01_2019-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2019-01-01_2020-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2020-01-01_2021-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2021-01-01_2022-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2022-01-01_2023-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2023-01-01_2024-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2024-01-01_2025-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2007-01-01_2008-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2008-01-01_2009-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2009-01-01_2010-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2010-01-01_2011-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2011-01-01_2012-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2018-01-01_2019-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2019-01-01_2020-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2020-01-01_2021-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2021-01-01_2022-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2022-01-01_2023-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2023-01-01_2024-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_ssh_2024-01-01_2025-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2015-01-01_2016-01-01.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2016-01-01_2017-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2015-01-01_2016-01-01_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2016-01-01_2017-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_noaa_nos_co_ops_9457804_temp_mean.png
---
name: 
---

```
````


+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2015-01-01_2016-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2016-01-01_2017-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_noaa_nos_co_ops_9457804_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## old-harbor-1


+++

### Sea surface height: mean subtracted

+++

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2015-01-01_2016-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2016-01-01_2017-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2017-01-01_2018-01-01_subtract-mean.png
---
name: 
---

```
````


+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2015



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2015-01-01_2016-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2016



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2016-01-01_2017-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_old-harbor-1_ssh_2017-01-01_2018-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````


+++

## wmo_46077


+++

### Sea water temperature: 

+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2007-01-01_2008-01-01.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2008-01-01_2009-01-01.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2009-01-01_2010-01-01.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2010-01-01_2011-01-01.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2011-01-01_2012-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2017-01-01_2018-01-01.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2018-01-01_2019-01-01.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2019-01-01_2020-01-01.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2020-01-01_2021-01-01.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2021-01-01_2022-01-01.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2022-01-01_2023-01-01.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2023-01-01_2024-01-01.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2024-01-01_2025-01-01.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2007-01-01_2008-01-01_subtidal.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2008-01-01_2009-01-01_subtidal.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2009-01-01_2010-01-01_subtidal.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2010-01-01_2011-01-01_subtidal.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2011-01-01_2012-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2017-01-01_2018-01-01_subtidal.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2018-01-01_2019-01-01_subtidal.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2019-01-01_2020-01-01_subtidal.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2020-01-01_2021-01-01_subtidal.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2021-01-01_2022-01-01_subtidal.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2022-01-01_2023-01-01_subtidal.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2023-01-01_2024-01-01_subtidal.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2024-01-01_2025-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_noaa_wmo_46077_temp_mean.png
---
name: 
---

```
````


+++

##### 2006



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2007



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2007-01-01_2008-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2008



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2008-01-01_2009-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2009



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2009-01-01_2010-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2010



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2010-01-01_2011-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2011



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2011-01-01_2012-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2017



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2017-01-01_2018-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2018



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2018-01-01_2019-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2019



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2019-01-01_2020-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2020



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2020-01-01_2021-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2021



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2021-01-01_2022-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2022



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2022-01-01_2023-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2023



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2023-01-01_2024-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2024



````{div} full-width                
```{figure} moorings_noaa_ciofs3/moorings_noaa_wmo_46077_temp_2024-01-01_2025-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

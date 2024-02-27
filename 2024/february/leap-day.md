## Feb 27th 2024

Leap day: https://github.com/rfordatascience/tidytuesday/tree/master/data/2024/2024-02-27

Everything is also saved in [this](https://app.hex.tech/katiesipos/app/7b7f75d9-076e-401d-8e69-4e414602036b/latest) Hex notebook. 


Import CSVs & save as dataframes. 

```python

import pandas as pd 
import plotly.express as px

births_df = pd.read_csv("births.csv")
deaths_df = pd.read_csv('deaths.csv')
events_df = pd.read_csv("events.csv")

```


# Save .dta files in python
import pandas as pd
df = pd.read_stata('my_data_in.dta')
df.to_stata('my_data_out.dta')

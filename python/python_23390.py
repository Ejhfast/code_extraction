# Use Groupby to construct a dataframe with value counts of other column
import pandas as pd
df = &lt;...&gt; #construct your dataframe
table = pd.crosstab(index=df.hour,columns=df.startneighborhood)

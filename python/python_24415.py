# How to get autoincrement values for a column after uploading a Pandas dataframe to a MySQL database
import pandas as pd
df['ID'] = pd.read_sql_query('select ifnull(max(id),0)+1 from db_table',cnx).iloc[0,0]+range(len(df))

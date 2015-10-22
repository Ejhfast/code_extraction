# Writing python (pandas) Data Frame to SQL Database Error
from sqlalchemy import create_engine
engine = create_engine('mssql+pyodbc://scott:tiger@mydsn')
df.to_sql('test', engine)

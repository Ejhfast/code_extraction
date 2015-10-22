# Pandas: Always selecting the first sheet/tab in an Excel Sheet
import pandas as pd
fd = 'file path'
data = pd.read_excel( fd, sheetname=0 )

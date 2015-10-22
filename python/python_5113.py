# use python to generate graph in excel
from win32com.client import Dispatch
ex = Dispatch("Excel.Application")
# you can use the ex object to invoke Excel methods etc.

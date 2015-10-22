# How do I call an Excel macro from Python using xlwings?
from xlwings import Workbook
wb = Workbook(...)
wb.application.xl_app.Run("your_macro")

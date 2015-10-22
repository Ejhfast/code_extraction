# How to get information from an xlsx file in Python?
from openpyxl import load_workbook
wb2 = load_workbook('email_contacts.xlsx')
print wb2.get_sheet_names()

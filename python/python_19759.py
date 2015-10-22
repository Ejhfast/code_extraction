# Currency objects being changed to a decimal.Decimal instance is used
import pythoncom
pythoncom.__future_currency__ = True # I guess it is True

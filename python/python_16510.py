# Siebel COM interface - Python
import win32com.client
oSiebelApp = win32com.client.Dispatch("SiebelDataControl.SiebelDataControl.1")
oSiebelApp.Login("Connection String")

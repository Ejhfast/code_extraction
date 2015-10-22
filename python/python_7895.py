# How do I create a .MDB and import a CSV into it using Python
import win32com.client
eng=win32com.client.gencache.EnsureDispatch("DAO.DBEngine.36")
eng.CreateDatabase("c:\\myNewAccessdB.mdb", win32com.client.constants.dbLangGeneral)

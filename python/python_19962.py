# Send keys to a inactive window in Python
hwndMain = win32gui.FindWindow("notepad", "prueba.txt: Bloc de notas")
hwndEdit = win32gui.FindWindowEx( hwndMain, 0, "Edit", 0 )
win32api.PostMessage( hwndEdit,win32con.WM_CHAR, ord('x'), 0)

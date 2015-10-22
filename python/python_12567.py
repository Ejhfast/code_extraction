# move mouse with python on windows 7
import win32api
def move_to(x,y):
    win32api.SetCursorPos((x,y))

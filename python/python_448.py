# Color picking from given coordinates
import win32gui
GetPixel(GetDC(WindowFromPoint( (XPos,YPos) )), XPos , YPos )

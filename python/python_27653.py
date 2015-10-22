# Send SIGINT in Windows using Python
from win32api import GenerateConsoleCtrlEvent
GenerateConsoleCtrlEvent(CTRL_C_EVENT, 0)

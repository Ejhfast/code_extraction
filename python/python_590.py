# retrieving current drive letters in windows (from python)
win32api.GetLogicalDriveStrings().split("\x00")

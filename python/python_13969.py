# How do I Open Windows Registry with write access in Python
key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject",0, wreg.KEY_ALL_ACCESS)

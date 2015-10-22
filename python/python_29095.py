# Python 3.4 plistlib doesn't work (str vs bytes errors)
with open("/Volumes/Thunderbay/CURRENT/Music/iTunes/iTunes Library.xml", 'rb') as itl:
    library = plistlib.load(itl)

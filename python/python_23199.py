# Removing Empty Line in a file without Removing Indentation Python
open('a_mod.py','w').write(''.join(l for l in open("a.py") if l.rstrip()))

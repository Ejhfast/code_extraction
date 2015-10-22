# replacing a string with SED
sed -i "/^class myClass2:/,/^class/s/f1 = '512kB'/f1 = '1MB'/" path/to/file.py

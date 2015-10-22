# Python: how to batch rename mixed case to lower case with underscores
sed -i -e :loop -re 's/(^|[^A-Za-z_])([a-z0-9_]+)([A-Z])([A-Za-z0-9_]*)'\
'([^A-Za-z0-9_]|$)/\1\2_\l\3\4\5/' -e 't loop' myFile.py

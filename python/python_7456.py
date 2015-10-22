# How to get filename from Content-Disposition in headers
import re
filename = re.findall("filename=(\S+)", f[1]['Content-Disposition'])

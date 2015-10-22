# Python How To Import And Use Module With One Line
from urllib.request import urlopen; print(int(str(urllib.request.urlopen("http://ir.eia.gov/ngs/wngsr.txt").read()).split("\\n")[4].split(" ")[2]))
#              note the semi-colon ^

# how do you search and replace in python
import re
server='web01.dc1.example.com'
re.sub(r"\..*$","",server)

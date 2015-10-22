# downloading an excel file from the web in python
import urllib
dls = "http://www.muellerindustries.com/uploads/pdf/UW SPD0114.xls"
urllib.urlretrieve(dls, "test.xls")

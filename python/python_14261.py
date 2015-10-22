# Fetching information from network projectors using python script
import urllib
stats_text = urllib.urlopen('http://ip.of.projector').read()

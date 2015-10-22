# Trace/BPT trap when calling urllib.urlopen
import urllib2
urllib2.install_opener(urllib2.build_opener())

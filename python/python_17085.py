# What is the best way to get the external IP of a machine in python?
import urllib2
myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()

# How can i grab some photos with python from website
with open("some_png.png","wb") as f:
     f.write(urllib2.urlopen("http://icons-search.com/img/yellowicon/TMNT_lin.zip/lin-png-256x256-Leonardo_256x256.png-256x256.png").read())

# Error while using urllib.request.urlopen in Python
&gt;&gt;&gt; from urllib.request import urlopen
&gt;&gt;&gt; for line in urlopen("http://google.com/"):
       print(line.decode("cp1251"))

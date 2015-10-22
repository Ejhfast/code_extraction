# extraction of file from filepath
from os.path import basename
print basename("/home/si/text.vx.txt").split('.')[0]
&gt;&gt;&gt; text

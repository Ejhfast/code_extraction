# Python XML regular expression matching issue
regex = re.compile('(?&lt;=&lt;)w:\w+(?=&gt;)|(?&lt;=&lt;)w:\w+(?=[\s\w+:\w+="[\w/:.-]+"]{0,10}&gt;)')

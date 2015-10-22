# How can I use this bash test construct in Python?
SVN = Popen('which svn 2&gt;&amp;1', shell=True, stdout=PIPE).communicate()[0]
str="if [[ ! -x " + SVN + " ]]; then echo 'svn could not be found or executed'; fi"
Popen(str, shell=True)

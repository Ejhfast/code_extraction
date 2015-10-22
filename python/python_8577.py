# I'm writing HTML files and I want a program that adds list item markup tags to a list of words
for line in open('tmp.txt'):
  print '&lt;li&gt;' + line.rstrip() +'&lt;/li&gt;'

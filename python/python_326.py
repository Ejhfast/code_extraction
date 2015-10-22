# How can I customize the output from pygments?
formatter = HtmlFormatter(style=MyStyle)
formatter.noclasses = True
print highlight(content,PythonLexer(),formatter)

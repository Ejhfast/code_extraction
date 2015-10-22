# lxml removes spaces and line breaks in <head>
parser = html5lib.HTMLParser(tree=html5lib.getTreeBuilder("lxml"), namespaceHTMLElements=False)

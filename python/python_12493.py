# How to check radio buttons and option list in PyQt4
doc = QWebView.page().mainFrame().documentElement()
male = doc.findFirst("input[id=signup-gender-male]")
male.setAttribute("checked", "true")

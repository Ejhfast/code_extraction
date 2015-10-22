# How can you parse xml in Google Refine using jython/python ElementTree
forEach(value.parseHtml().select("dc|identifier"),v,v.htmlText()).join(",")

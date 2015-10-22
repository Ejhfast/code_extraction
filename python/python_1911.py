# How to convert this regular expression into Python
def removeHtmlTags(page):
    p = re.compile(r'''&lt;(?:"[^"]*"['"]*|'[^']*'['"]*|[^'"&gt;])+&gt;''')
    return p.sub('', page)

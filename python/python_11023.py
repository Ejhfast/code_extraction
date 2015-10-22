# parseerror in jQuery when returning xml from mod_python
def method(req):
    req.content_type = 'text/xml'
    req.write('&lt;items&gt;&lt;item&gt;1&lt;/item&gt;&lt;item&gt;2&lt;/item&gt;&lt;/items&gt;')

# can iceweasel automatically go "back" when it loads an error page
def notfound():
    return web.notfound("&lt;script&gt;window.location="http://some.com";&lt;script&gt;")

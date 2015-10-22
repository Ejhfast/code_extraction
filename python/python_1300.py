# How to get the html source of a specific element with selenium?
sel = selenium('localhost', 4444, browser, my_url)
html = sel.get_eval("this.browserbot.getCurrentWindow().document.getElementById('1').innerHTML")

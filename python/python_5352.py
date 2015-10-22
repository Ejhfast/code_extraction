# PyQt QWebKit frame bug?
def Load(self):
    self.webView.page().setViewportSize(
        self.webView.page().mainFrame().contentsSize())

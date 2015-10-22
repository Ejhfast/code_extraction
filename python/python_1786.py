# QWebView not loading external CSS
path = os.getcwd()
self.webview.settings().setUserStyleSheetUrl(QUrl.fromLocalFile(path + "/myCustom.css"))

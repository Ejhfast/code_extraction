# How to set user-agent in python-webkit
settings = webkit.WebSettings()
  settings.set_property('user-agent', 'iPad')
  webview.set_settings(settings)

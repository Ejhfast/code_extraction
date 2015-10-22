# How to Force File Download on Twisted HTTP Server?
request.responseHeaders.setRawHeaders(
    'Content-Disposition', ['attachment; filename="foo"'])

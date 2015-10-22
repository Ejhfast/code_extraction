# Using a Unicode format for Python's `time.strftime()`
fmt = u'%d\u200f/%m\u200f/%Y %H:%M:%S'
time.strftime(fmt.encode('utf-8'), &lt;your time here&gt;).decode('utf-8')

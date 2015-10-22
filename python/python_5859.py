# How do I convert a file stream to a data URI in Python?
&gt;&gt;&gt; '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x04\x87...'.encode('base64').replace('\n', '')
'iVBORw0KGgoAAAANSUhEUgAABI....'

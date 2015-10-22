# A Unicode string written in escaped ASCII
&gt;&gt;&gt; u'Syst\xc3\xa8me'.encode('latin-1').decode('utf-8')
u'Syst\xe8me'

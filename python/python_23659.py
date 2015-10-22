# Character encoding in python to replace 'u2019' with '
&gt;&gt;&gt; import unidecode
&gt;&gt;&gt; unidecode.unidecode(u'BACK RUSHIN\u2019')
"BACK RUSHIN'"

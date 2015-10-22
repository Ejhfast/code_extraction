# When calling a Python script from a PHP script, temporary file that is created on a console run, is not created via the PHP invocation
passthru('/usr/python/bin/python3 ../cgi-bin/tabular.py 1 2&gt;&amp;1');

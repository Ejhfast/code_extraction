# is it possible to have optional parameters in templates in web.py
$def with(**kwargs)
$if kwargs['error']:
    &lt;p class=error&gt;$kwargs['error']&lt;/p&gt;

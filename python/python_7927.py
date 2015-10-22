# django - reusing a login template
(r'^my_url/$', 'login', {'redirect': admin}),
(r'^my_other_url/$', 'login', {'redirect': beta}),

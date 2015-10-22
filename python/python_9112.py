# How do I rewrite this URL in Django?
('^servertest/(?P&lt;path&gt;.*)$', 'redirect_to', {'url': '/server-test/%(path)s'}),

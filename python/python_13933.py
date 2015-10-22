# Test page for mod_wsgi
def application(env, respond):
    respond('200 OK', [('Content-Type', 'text/plain')])
    return ['\n'.join('%s: %s' % (k, v) for (k, v) in env.iteritems())]

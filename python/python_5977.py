# Google App Engine Python simplejson escaping?
if json.encoder.ESCAPE_DCT.get('/') != '/':
    json.encoder.ESCAPE_DCT['/'] = '/'

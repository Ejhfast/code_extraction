# Bottle and Json
@route('/api/status')
def api_status():
    return {'status':'online', 'servertime':time.time()}

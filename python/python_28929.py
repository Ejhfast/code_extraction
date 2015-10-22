# Google App Engine Edge Cache not working
response.headers['Pragma'] = 'Public'
response.headers['Cache-Control'] = 'public, max-age=%d'%time

# requests url encoding for multi-valued parameters
In [54]: urllib.unquote(google_response.url).decode('utf8')
Out[54]: u'http://maps.googleapis.com/maps/api/directions/json?origin=40.970321,29.060873&amp;destination=28.974656,41.029967&amp;sensor=false'

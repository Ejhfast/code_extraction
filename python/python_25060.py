# How to output a live JSON feed in Python 3?
quake_data = requests.get('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson').json()
print(quake_data['metadata']['title'])

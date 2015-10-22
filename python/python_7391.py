# Cannot JSON serialize python Appengine GeoModel subclass using simple json
return json.dumps({'lat': result.lat, 'lon': result.lon})

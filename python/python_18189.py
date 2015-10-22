# I dont understand how to feed pygeocoder a variable instead of straight up number
point = []
point.append([45.424571, -75.695661])
results = Geocoder.reverse_geocode(*point[0])

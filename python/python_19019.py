# Extract latitude and longitude from coordinates
for index in range(len(col)):
    lat, lon = col[index].split(",")
    print "lat=%s, lon=%s" % (lat, lon)

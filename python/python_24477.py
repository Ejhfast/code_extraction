# Nested SELECT vs INNER JOIN
latlongs = LatLong.objects.filter(date__gte=time1, date__lte=time2, vehicle__omei=omei)

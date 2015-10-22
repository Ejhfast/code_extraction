# Using GPXPY to parse gpx file results in not well-formed invalid token error
import gpxpy
f = open(path_to_gpx_file, 'r')
p = gpxpy.parse(f)

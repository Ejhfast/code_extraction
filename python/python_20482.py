# Convert from SRS coordinates to Latitude and Longitude in Python
echo 501343.42 4137351.57  | cs2cs -f "%.6f" +init=epsg:25830 +to +init=epsg:4326

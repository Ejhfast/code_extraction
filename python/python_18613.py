# How to add multiple files automatically in BASH?
FILE=`find ~/Desktop/folder -name '*.tif'`
gdal_merge.py -o mosaic -of GTiff "$FILE"

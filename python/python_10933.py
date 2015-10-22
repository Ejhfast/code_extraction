# stderr (from GDAL) not shown in Python shell
from osgeo import gdal
gdal.UseExceptions()
gdal.Open('myfile.tif")

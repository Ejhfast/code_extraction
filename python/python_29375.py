# programatically list all variables of a netCDF file using netCDF4 and python
import netCDF4
dset = netCDF4.Dataset('test.nc')
dset.variables

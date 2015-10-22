# How to check blas/lapack linkage in numpy/scipy?
import numpy.distutils.system_info as sysinfo
sysinfo.get_info('atlas')

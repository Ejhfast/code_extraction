# F2PY doesn't find a module
f2py -c --fcompiler=gfortran -I"path-to-dir-with-mod-files" --fcompiler=gfortran -I"path-to-dir-with-mod-files" -lNESDIS_LandEM_Module -m mod_landems mod_landem.f90 -m mod_landems mod_landem.f90

# python in mac os x error Undefined symbols: "_PyImport_Import"
export CPPFLAGS="$CPPFLAGS -I/opt/local/include"
 export LDFLAGS="$LDFLAGS -L/opt/local/lib -lpython2.7"
./configure --with-fox=/opt/local --with-proj-gdal=/opt/local --with-xerces=/opt/local --prefix=/opt/sumo --with-python

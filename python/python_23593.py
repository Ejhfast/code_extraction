# Error installing bcrypt with pip on OS X: cant find ffi.h (libffi is installed)
$ brew install pkg-config libffi
$ export PKG_CONFIG_PATH=/usr/local/Cellar/libffi/3.0.13/lib/pkgconfig/
$ pip install bcrypt

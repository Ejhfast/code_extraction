# Setup Eclipse to work with Python bindings for Subversion
mkdir python-libdir/site-packages/pysvn
cp pysvn/__init__.py python-libdir/site-packages/pysvn
cp pysvn/_pysvn*.so python-libdir/site-packages/pysvn

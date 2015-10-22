# Python ImportError - undefined symbol - for custom C++ module
g++ -fPIC -shared -o mymodule.so mymodule.cpp `pkg-config --cflags --libs python` `pkg-config --cflags --libs opencv` -I/usr/local/include/opencv2/legacy

# Virtualenv __future__ module works on command line, but not while running dev_appserver.py
$ cd /usr/local/google_appengine/google/appengine/tools
$ wget "http://googleappengine.googlecode.com/issues/attachment?aid=43390029000&amp;name=dev_appserver_import_hook.patch&amp;token=974d9f138a5604dc7eb0526156b26cc7" -O dev_appserver.patch
$ patch -p1 &lt; dev_appserver.patch

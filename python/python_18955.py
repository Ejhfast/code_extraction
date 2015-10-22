# import python packages from a zip file in c/c++ standalone application
&gt;&gt;&gt; import sys
&gt;&gt;&gt; sys.path.insert(0, 'example.zip')  # Add .zip file to front of path
&gt;&gt;&gt; import foobar

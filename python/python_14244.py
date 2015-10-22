# How can a shell function know if it is running within a virtualenv?
python -c 'import sys; print sys.real_prefix' 2&gt;/dev/null &amp;&amp; INVENV=1 || INVENV=0

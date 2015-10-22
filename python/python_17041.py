# Proper permissions for python packages
umask 0022 &amp;&amp; chmod -R a+rX . &amp;&amp; python setup.py sdist upload

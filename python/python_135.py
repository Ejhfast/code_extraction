# How to include output of PHP script in Python driven Plone site?
import os
print os.popen('php YourScript.php').read()

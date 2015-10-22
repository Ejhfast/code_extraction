# How to save web page as image using python
import subprocess
subprocess.Popen(['wget', '-O', MYFILENAME+'.png', 'http://images.websnapr.com/?url='+MYURL+'&amp;size=s&amp;nocache=82']).wait()

# How to prevent fabric form waiting for the process to return
sudo("python test.py  2&gt;/dev/null &gt;/dev/null &amp;")

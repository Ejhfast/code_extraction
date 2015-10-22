# Starting multiple instances of a python script at once from linux command line
for i in {1..1000}; do nohup python test.py &amp; done

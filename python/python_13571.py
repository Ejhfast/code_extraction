# How to set a python path when using runit
#!/bin/sh
export PYTHONPATH=$PYTHONPATH:/home/ubuntu/workspace/htFrontEnd/heythat:/home/ubuntu/workspace/htFrontEnd/heythat/htanalytics
exec /usr/bin/python /home/ubuntu/workspace/htFrontEnd/htanalytics/ht_rpc_server.py &gt;&gt; /tmp/ht_rpc_server.log 2&gt;&amp;1

# One line command to clear 8000 open port, killing django development server that run on background
netstat -tulpn |grep 8000|awk '{print $7}'|cut -d/ -f 1|xargs kill

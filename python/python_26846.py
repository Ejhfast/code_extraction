# declaring bash variable from parsing JSON with curl and python
SERVICE=$(curl -s http://10.10.1.10/api/ping | python -c 'import sys, json; print json.load(sys.stdin)["service"]')

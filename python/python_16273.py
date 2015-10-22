# how to dump http traffic?
tshark -l -f "tcp port 80" -R "http.request or http.response " -i br0 -V

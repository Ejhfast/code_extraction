# acting like a switch between two sockets with python
ncat -o dump -l 192.168.10.159 35621 --sh-exec "ncat 192.168.10.40 9000"

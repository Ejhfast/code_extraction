# How to start IPython notebook remotely?
# Login to the server from your local workstation and in the same connection do the port forwarding.
user@local$ ssh -L 8888:localhost:8889 username@remote_host
user@remote_host$ ipython notebook --no-browser --port=8889

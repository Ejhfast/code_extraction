# SSH to a server and exit Python script (in the same shell)
#!/bin/sh
export $(credentials.py)
exec ssh hostname

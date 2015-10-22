# Fabric will stop redis server but it will not start it again
sudo('service redis_6379 start', pty=False)

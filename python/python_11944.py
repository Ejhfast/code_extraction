# How to target a different host inside a Fabric command
from fabric.context_managers import settings
with settings(host_string='remote_server'):
    run('ls -lart')

# is there a way to use fabric run() and sudo() at a time?
from fabric.api import cd,sudo
with cd('somepath'):
    sudo('./execute_script.sh')

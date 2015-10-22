# Setting fabric hosts list from an external hosts file
def set_hosts():
    env.hosts = open('hosts_file', 'r').readlines()

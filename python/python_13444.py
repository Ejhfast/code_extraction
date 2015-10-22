# how to run automation task in different group using fabric
def update_hosts():
    execute(get_last_hosts)
    execute(upload_hosts)

# Select from MySql with a variable
cur_syslog.execute("SELECT data FROM firewall WHERE source_ip = %s", (ip))

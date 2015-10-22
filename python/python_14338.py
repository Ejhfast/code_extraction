# python - get hostname values from each line /etc/hosts
for line in hosts:
        print line.split()[1:]

# Rebalancing after failover a couchbase node
payload = {'ejectedNodes': 'ns_1@10.90.150.21', 'knownNodes': 'ns_1@10.90.150.21,ns_1@10.90.150.22,ns_1@10.90.150.23'}
requests.post(url, data=payload, auth=(un, pwd))

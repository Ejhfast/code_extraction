# Find the nodes in the percona cluster
engine.execute("SHOW VARIABLES LIKE 'wsrep_cluster_address'").fetchone()

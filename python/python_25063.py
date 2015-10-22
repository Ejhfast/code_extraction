# Cannot perform a backup or restore operation within a transaction
conn.autocommit = true
// do stuff
conn.autocommit = false

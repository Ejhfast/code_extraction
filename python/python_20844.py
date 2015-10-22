# How do you return the timestamp from Cassandra when using Python and CQL?
return datetime.utcfromtimestamp(int64_unpack(byts) / 1000.0)

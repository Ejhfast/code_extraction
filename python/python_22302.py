# Is there a way to pass in a parameter for matching on labels in neo4j
MATCH (n)
WHERE {z} IN labels(n)
RETURN n

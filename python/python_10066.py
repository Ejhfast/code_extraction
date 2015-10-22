# Multiple-column keys with SQLAlchemy
SELECT coalesce(max(ID_B),0)+1
FROM yourTable
WHERE ID_A = '1'

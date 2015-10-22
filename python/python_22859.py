# Add MySQL query results to R dataframe
queries=sprintf("SELECT value as value FROM %s FORCE INDEX (chrs) FORCE INDEX (sites) WHERE chrom = %d AND site = %d UNION ALL SELECT 0 LIMIT 1", "TableName", df$Chrom, df$Pos)
df$Value = do.call("rbind",sapply(queries, function(query) dbSendQuery(mydb, query)))$value

# sqlite how to optimize query for Nth percentile
cursor.executescript("SELECT COUNT(value) AS itemcount FROM history WHERE itemid=?; \
    SELECT value FROM history WHERE itemid = ? ORDER BY value ASC LIMIT 1 OFFSET itemcount * (? / 100) - 1)", \
    [itemId, itemId, percentile])

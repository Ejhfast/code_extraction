# "Flexible" MySQL limit
SELECT whatever FROM comments_table c
WHERE c.id IN (SELECT id FROM comments_table c2 WHERE some_criteria_here LIMIT 10)
OR c.parent_id IN (SELECT id FROM comments_table c2 WHERE some_criteria_here LIMIT 10)

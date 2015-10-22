# Django model group by more than 2 elements
SELECT rating, COUNT(rating) AS rc, COUNT(DISTINCT userid) FROM rating_tbl GROUP BY rating ORDER BY rc DESC;

# Python sqlite3 misinterpreting parameter
SELECT x, y, 'valid_field_name' FROM literal_table
WHERE 'valid_field_name' &gt; 0 AND (some other conditions)
GROUP BY x, y

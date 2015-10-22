# SQL SERVER : find list of records in one select query that are not in another select query
SELECT ROW,COLUMN FROM TABLE1 WHERE STAGE = 130.0
    EXCEPT
    SELECT ROW,COLUMN FROM TABLE1 WHERE STAGE = 120.0

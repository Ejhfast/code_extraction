# MySQL Avoiding duplicates in table of unknown column headers
ALTER IGNORE TABLE MyTable ADD UNIQUE INDEX idx_name (name, age);

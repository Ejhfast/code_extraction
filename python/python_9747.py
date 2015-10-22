# PostgreSQL: Running Python stored procedures as a normal user
UPDATE pg_language SET lanpltrusted = true WHERE lanname = 'plpythonu';

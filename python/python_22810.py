# How do I express a function that returns a setof record in sqlalchemy?
&gt;&gt; print sa.select().select_from('a AS f(a int, b int)')
SELECT
FROM a AS f(a int, b int)

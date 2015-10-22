# Python: get escaped SQL string
cur.mogrify("SELECT * FROM foo WHERE foo.bar = %s", ("foo 'bar' \"baz",))

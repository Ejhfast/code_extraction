# How to ensure sqlite db connections get closed during debugging?
with sqlite.connect(...) as db:
    with db.cursor() as c:
        ...

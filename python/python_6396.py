# Python: apply list in nested function call
c.executemany(strQuery, rows(
    *[readfile(afiles_dt[f][0]) for f in range(len(afiles_dt))]
))

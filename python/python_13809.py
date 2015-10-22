# Only import two columns from a CSV
con.executemany("insert into stats(date, temperature) values (?, ?)",
                ((rec[0], rec[9]) for rec in stats))

# Python MySQL connector, "wrong number of arg.."
job_insert = "INSERT INTO f.job (customer, period, cost) VALUES ('{0}', {1}, {2});".format(job['customer'], job['period'], job['cost'])
cursor.execute(job_insert)
cursor.execute('commit')

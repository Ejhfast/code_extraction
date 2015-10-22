# Query for repeated ndb.KeyProperty not working
applicants = Applicants.query(Applications.position==position.key).fetch()

# Python, Beatbox - Return all available fields
desc = svc.describeSObjects("Account")
    for f in desc[sf.fields:]:
        print "\t" + str(f[sf.name])

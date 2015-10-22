# How can this be written on a single line?
errs = dict((f.auto_id, f.errors) for f in form if f.errors)

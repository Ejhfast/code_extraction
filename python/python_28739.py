# Multiple forms in the same page, keep data populated when submitting
if request.form.getlist('submit_criteria'):
      del request.form

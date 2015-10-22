# Form validation with WTForms and and autofill SQLAlchemy model with form data in Flask
if form.validate_on_submit():
    campaign = Campaign()
    form.populate_obj(campaign)

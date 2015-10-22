# Using Pylons validate and authenticate_form decorator
@validate(schema=MeowForm(), form='index')
@authenticate_form
def do_post(self):

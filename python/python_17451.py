# using form in web2py SQLFORM.factory and adding 2 require for same field
form = SQLFORM.factory(
    Field('email', requires=[IS_NOT_EMPTY(), IS_EMAIL(error_message='invalid email')])
    )

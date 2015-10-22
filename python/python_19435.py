# How to append my own error to the ErrorDict of a form in Django?
form._errors["user_name"] = form.error_class([u'This username is registered.'])

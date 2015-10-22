# django - view returning no value?
return JSONResponse(operator.attrgetter('user_permissions', 'username', 'first_name')(request.user))

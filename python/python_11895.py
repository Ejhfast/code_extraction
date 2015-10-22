# Web2py - preventing uploaded file content from appearing in URL when using redirect() with request.vars
del request.vars.file
redirect(URL('form2', vars=request.vars))

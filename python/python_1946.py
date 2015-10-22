# Python | How to send a JSON response with name assign to it
jsonValidateReturn = simplejson.dumps({'jsonValidateReturn': array_to_js})
return HttpResponse(jsonValidateReturn, mimetype='application/json')

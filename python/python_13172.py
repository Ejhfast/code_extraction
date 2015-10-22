# How to check for the existence of a get parameter in flask
opt_param = request.args.get("something")
if opt_param is None:
    print "Argument not provided"

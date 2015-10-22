# Remove the namespace from Spyne response variables
def _method_return_string(ctx):
    ctx.out_string[0] = ctx.out_string[0].replace("tns:result&gt;", "result&gt;")
    ctx.out_string[0] = ctx.out_string[0].replace("tns:notify&gt;", "notify&gt;")

# Output all variables into Mako template
${context.keys()}    # list of direct variable names
${context.__dict__}  # probably more along what you're looking for.

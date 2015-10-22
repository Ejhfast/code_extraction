# if loop syntax error
if any(x in line for x in ('SU', 'AU', 'VU', 'rf')) and '/*' not in line and BUILDROOT in line:
    lineMatch = False

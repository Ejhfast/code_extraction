# Regex: match "group3.*group1" if group2 is not between groups 3 and 1
^.*?(?:g31|g32)(?!.*?(?:g21|g22)).*?(?:g11|g12).*$

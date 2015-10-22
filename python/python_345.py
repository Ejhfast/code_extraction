# How should I conditionally assign based on the existence of a dictionary key?
message = "%s was a match"%(matches[key],) if key in matches else "There was no match."

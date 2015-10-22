# How to rstrip only when the object is not "None type"
if build_loc is not None:
    Target_list.append(build_loc.rstrip('\r\n'))

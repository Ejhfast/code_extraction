# How do I start reading a file from the top in python?
file_content = set([line.rstrip() for line in file_handler])
only_in_platform = set(platform_specific_req).difference(file_content)

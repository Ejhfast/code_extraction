# Change path's in yaml files
output = re.sub(r"\.\./(?=\w)(?!id)", "../Sys/", input)

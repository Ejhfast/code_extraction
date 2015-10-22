# Constructing an expression
" OR ".join(["%s branch:%s"%(line.strip(),getbranch_project(line.strip())) for line in f])

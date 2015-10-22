# In python exclude folders which start with underscore or more than six characters long
folders = [name for name in os.listdir(".")
           if os.path.isdir(name) and name[0] != '_' and len(name) &lt;= 6]

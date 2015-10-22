# Fabric, retrieving result of a bash command into a python variable
a = sudo("ls -l my_filename | awk '{print $11}'", capture=True )

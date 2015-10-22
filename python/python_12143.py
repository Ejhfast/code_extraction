# gunicorn - not taking config file if executed from shell script
#!/bin/bash
source /path/to/active
gunicorn_django -c $(pwd)/path/to/conffilefrom/presentworkingdirectory -D

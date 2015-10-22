# Python egg found interactively but not in fastcgi
#!/bin/sh
export PYTHONPATH=/your/local/python/path
/path/to/python /path/to/your/fastcgi/handler  # this line should be similar to what was supplied to mod_fastcgi originally

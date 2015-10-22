# Apache: dynamically interpret static files
AddHandler x-application/mako-template .mako
Action x-application/mako-template /mako-handler
WSGIScriptAlias /mako-handler /usr/local/lib/cgi-bin/myscript.py

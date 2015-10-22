# TextMate Python bundle non-blocking
subprocess.Popen('$HOME/.virtualenvs/supervisor/bin/' \
                     'supervisorctl restart {0}'.format(projname),
                     shell=True, close_fds=True, stdout=open('/dev/null', 'w'))

# Only one instance of background task in uWSGI and gevent environment
# spawn only if i am worker 1
if uwsgi.worker_id() == 1: spawn()

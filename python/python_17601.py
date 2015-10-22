# Why are Python webservers unstable?
USER -&gt; BALANCER (nginx,apache,ecc) -&gt; APPSERVER (uwsgi, twisted, gunicorn, ..) -&gt; WSGI Application

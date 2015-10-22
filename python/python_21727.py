# Django serving media files (user uploaded files ) in openshift
RewriteEngine On
RewriteRule ^application/media/(.+)$ /static/media/$1 [L]

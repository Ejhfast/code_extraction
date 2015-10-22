# Apache2 redirect to central cgi script
RewriteEngine On
RewriteCond %{REQUEST_URI} !^(/index.py|/downloads)
RewriteRule ^(.*)$ /index.py?url=$1

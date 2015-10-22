# django dynamic file serving optimization
RewriteCond %(REQUEST_URI) ^media
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule #Some rewrite rule to redirect from '/media/filename' to '/image_generator/filename'

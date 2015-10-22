# Nginx: Mapping WordPress URLs to new static website
location ~ "^/[\d]{4}/[\d]{2}/(.*)$"   {return 301 $scheme://$host/posts/$1;}

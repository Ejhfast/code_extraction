# django sphinx search always get none from query
ps auxw | grep httpd | awk '{print"-p " $2}' | xargs strace

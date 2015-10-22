# django serving robots.txt efficiently
location  /robots.txt {
    alias  /path/to/static/robots.txt;
}

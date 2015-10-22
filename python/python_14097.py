# (nginx + uWSGI + Bottle) Serve static Files
location /assets/ {
  alias pathtoyourproject/ROOT/assets/;
}

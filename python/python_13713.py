# GAE Python: Images working on localhost but not working after deploy
- url: /static/images/(.*\.(gif|ico|jpeg|jpg|png))
  static_files: static/images/\1
  upload: static/images/(.*\.(gif|ico|jpeg|jpg|png))

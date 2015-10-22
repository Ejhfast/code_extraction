# Configuring Python GAE app.yaml for Static Files
- url: /.*?([^/]*\.css)
  static_files: css/\1
  upload: css/.*\.css

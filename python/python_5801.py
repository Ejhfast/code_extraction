# How to write static_files exclude one subdirectory in yaml of Google App Engine
- url: /foo/bar/([^.]+\.(js|css))
  static_files: foo/bar/\1
  upload: foo/bar/[^.]+\.(js|css)

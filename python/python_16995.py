# Show 404 when specific route matches
if not os.path.exists(os.path.join(template_path, page)):
    self.abort(404)

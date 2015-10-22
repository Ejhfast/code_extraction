# Add new "plugin" to Flask app in runtime
app.register_blueprint(imported_plugin.plugin_handler, url_prefix=imported_config.FOO)

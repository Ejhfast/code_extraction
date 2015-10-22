# Flask route query parameter
app.add_url_rule('/example', view_func = example.Index.as_view('example_index'))
app.add_url_rule('/example/&lt;string:example_key&gt;', view_func = example.Show.as_view('example_show'), methods=['GET'])

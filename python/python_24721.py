# Is there a way to pass parameter for textarea-rows from database to html
Field('title', 'text', label=T('Please enter something:'),
      widget=lambda f, v: SQLFORM.widgets.text.widget(f, v, _rows=5))

# python flask app validate text field - allow no space
username = TextField('Username', [validators.Regexp(r'^[\w.@+-]+$'), validators.Length(min=4, max=25)])

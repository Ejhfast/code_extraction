# decode self.request.body
&gt;&gt;&gt; import urllib
&gt;&gt;&gt; urllib.unquote_plus("%7B+%22name%22%3A+%22John+Dao%22%2C+%22Age%22%3A+42+%7D=")
'{ "name": "John Dao", "Age": 42 }='

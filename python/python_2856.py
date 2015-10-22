# Elixir/SQLAlchemy equivalent to SQL "LIKE" statement?
&gt;&gt;&gt; Note.query.filter(Note.message.like("%somestr%")).all()
[]

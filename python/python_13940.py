# Prefetch column sequence SQLAlchemy
seq = Sequence('some_sequence')
nextid = connection.execute(seq)

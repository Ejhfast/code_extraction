# python sqlite3 update not updating
cur.execute('UPDATE workunits SET Completed=1, Returns=? WHERE PID=? AND Args=?',
    (pickle.dumps(Ret), PID, Args)
)

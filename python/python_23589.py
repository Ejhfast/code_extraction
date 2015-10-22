# Python-handler-socket (pyhs) update function example
# UPDATE mydb.test1 SET Cnt=5 WHERE Id=1
hs.update('mydb', 'test1', '=', ['Id', 'Cnt'], ['1'], ['1', '5'])

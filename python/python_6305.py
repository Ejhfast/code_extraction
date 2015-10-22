# SQLAlchemy: Hybrid Value Object, Query Tuple Results
for row in session.query(MyClass.mycustomthing, MyClass.myothercustomthing):
   print row.word, row.someotherword

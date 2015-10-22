# SQL Date Variables in Python
query2 ="""insert into table xyz(select * from abc where date_time = %s)"""
cur.execute(query2,(rows))

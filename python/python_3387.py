# How to bulk insert data to mysql with python
conn.execute(Product.insert(), [dict(name=name) for name in names])

# SQLAlchemy: How to change a MySQL server system variable using SQLAlchemy?
# change variable name and values to what you need
connection.execute("SET SESSION query_cache_type = OFF")

# How to update multiple rows with single MySQL query in python?
cur.executemany("UPDATE Writers SET Name = %s WHERE Id = %s ",
        [("new_value" , "3"),("new_value" , "6")])

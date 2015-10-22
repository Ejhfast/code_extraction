# Python web.py error OperationalError: near "name": syntax error
DBsearch = LjDB.execute("select * from caiji where post like ?",
                        ('%{}%'.format(searcher),))

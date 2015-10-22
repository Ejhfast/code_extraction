# how can I make 'between' query with web2py.DAL?
db((db.mytable.create_date&gt;=query_dict['create_date1'])&amp;(db.mytable.create_date&lt;=query_dict['create_date2'])).select()

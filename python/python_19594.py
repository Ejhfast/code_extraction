# Flask SQLite query
g.db.execute('update address set firstname=?,surname=?,email=?,mobile=? where contact_id = ?',\
                (request.form['firstname'], request.form['surname'],\
                request.form['email'], request.form['mobile'],contact_id))

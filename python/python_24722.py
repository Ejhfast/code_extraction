# How to store and access values stored in a Session Object on separate form pages
request.session['fav_color'] = 'red' #Set the value
fav_color = request.session.get('fav_color', 'red') #Read the value else read a default one

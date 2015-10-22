# what is the best filter to query a full name datastore property using only the first name?
p.filter('person_name &gt;=', searched_name)
p.filter('person_name &lt;', searched_name + u'\ufffd')

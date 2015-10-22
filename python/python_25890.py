# How to check if entity exist in gae datastore?
greetings_query = Greeting.query(
        ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
 greetings = greetings_query.fetch(10)

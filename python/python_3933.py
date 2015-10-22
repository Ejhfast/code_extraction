# Load list with content of object
items = [{'category': m.category, 'message': m.message}
  for m in h.flash.pop_messages()]

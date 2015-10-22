# Parse email and get number from body
for part in email.iterators.typed_subpart_iterator(msg, 'text', 'plain'):
   for body_line in email.iterators.body_line_iterator(part):
       print body_line

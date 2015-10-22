# Create a receipt for a user form submission
hash = h(h(username) + month + year + h(salt))

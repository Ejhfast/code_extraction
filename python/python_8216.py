# Foreach comma separated item
shares = parser.get('profile', 'shares')
for share in shares.split(', ')
    username = parser.get(share, 'username')

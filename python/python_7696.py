# How to get objects if user is in a field of another django model's many-to-many field?
Project.objects.filter(node__collaborators=my_user)

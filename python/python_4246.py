# How can I get all objects a user has specific permissions to in django guardian?
from guardian.shortcuts import get_objects_for_user
...
videos = get_objects_for_user(request.user, "view_video", Video.objects.all())

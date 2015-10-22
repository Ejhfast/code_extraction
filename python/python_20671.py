# Caught SyntaxError while rendering: invalid syntax
story_list = Story.objects.filter(Q(title__contains=term) | Q(markdown_content__contains=term))

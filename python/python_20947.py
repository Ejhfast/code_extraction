# Creating mptt from a django model
category_l1_array = list(set(deg_course_cat.objects.filter(degree_code=degree[i]).values_list('category_level1', flat=True)))

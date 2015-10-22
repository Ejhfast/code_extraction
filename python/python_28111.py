# How to reverse query objects for multiple levels in django?
Level4.objects.filter(level3__level2__level1=my_level1_object)

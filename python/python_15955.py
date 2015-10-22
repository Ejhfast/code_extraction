# Join strings with "and" depending on single or plural result
list_of_objects = [Obj1, Obj2, ... ObjN]
" and ".join([obj.name for obj in list_of_objects])

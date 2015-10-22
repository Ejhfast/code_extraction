# How to check if an object in a list has a certain property
if any(obj.type == 'type 1' for obj in object_list):
    object_list = [obj for obj in object_list if obj.name != 'some_name']

# Using MongoDB, how do you remove embedded document from a list based on a match
Main.objects(id=main_id).update_one(pull__values__id = Sub(Id=sub_id) )

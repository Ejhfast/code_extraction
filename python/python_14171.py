# How to iterate through a list of dictionaries & pick one highest value
result = max( the_list, key=lambda item:item['likes']['count'] )

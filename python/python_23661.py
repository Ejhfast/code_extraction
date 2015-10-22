# Accessing elements in dictionary of dictionaries
inner_dict = places["City"]
for _, city_obj in inner_dict.items():
    print city_obj.population # Assuming population is one of the member variables of the class mod.city

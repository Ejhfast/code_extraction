# Sorting ManyToMany field automatically in Django model
pizza.toppings.order_by('topping_relationship__order_to_add_topping')

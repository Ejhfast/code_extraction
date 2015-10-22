# python TraitsUI variable number of items in view
view=View(Item(name='muffin_type'),
          Item(name='type_of_blueberry',editor=BlueberryEditor(),
               visible_when='muffin_type==\'blueberry\'')))

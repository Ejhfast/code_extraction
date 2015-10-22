# Pymongo search geo on line
collection.find({'loc':{'$within':{'$polygon':[[linestart_x, linestart_y], [linestart_x+jiggle, linestart_y+jiggle], [lineend_x, lineend_y], [lineend_x+jiggle, lineend_y+jiggle]]}}})

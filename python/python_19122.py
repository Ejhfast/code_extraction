# use boolean list as mask
["not " * (1 - x) + y.obj_dict['self'].get_topic() for x,y in zip(comb, self.parents)]

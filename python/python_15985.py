# Python to JSON Serialization
new_dict = dict([(attr,self.__dict__[attr]) for attr in self.__dict__ if self.__dict__[attr]])
return json.dumps(new_dict, default=lambda obj: obj.__dict__, indent=4)

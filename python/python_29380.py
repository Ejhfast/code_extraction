# Object instance evocation by provided variable
objects = {4: oven, 8: delta_t_pause, 15: caliberBox}
if senderid in objects:
    obj = objects[senderid](data)

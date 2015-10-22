# Is it possible to have variable dot accessors in Python 2.6 / Django1.3?
for x in ['foo', 'bar', 'ray', 'mee']:
    random_list.append(getattr(model_instance, x))

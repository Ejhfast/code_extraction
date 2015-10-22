# shorthand way to create dictionary key if it does not exist
def add_to_world(self, species, name, zone = 'retreat'):
    self.object_attr.setdefault(species, {})[name] = {'zone' : zone}

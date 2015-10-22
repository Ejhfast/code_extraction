# Python2.7: Trying to pickle set of custom objects
with open(os.path.join(asset_path, "frame_jar.pkl"), 'rb') as infh:
    unpickler = cPickle.Unpickler(infh)
    self.scene_surfaces = unpickler.load()

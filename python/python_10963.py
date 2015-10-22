# How do I call a plugin module that's loaded?
mod = imp.load_source("MyModule", "MyModule.py")
   clz = getattr(mod, "MyClassName")

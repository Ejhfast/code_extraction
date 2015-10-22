# Hot swapping python code (duck type functions?)
mod = __import__(module_name)
fn = getattr(mod, fn_name)
fn()

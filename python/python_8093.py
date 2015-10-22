# Make a function live "inside" a module
fn = new.function(c.to_code(), module.__dict__, name.name)

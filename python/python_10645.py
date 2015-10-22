# Is it possible to introspect actual attributes/methods of an object which overrides `__dir__` and `__getattribute__`?
object.__getattribute__(instance, '__dict__')

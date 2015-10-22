# How can I create bound methods with type()?
Spam = type("Spam", (Foo, ), {"echo":echo})
spam = Spam()
spam.echo()

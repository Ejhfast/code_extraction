# python sqlalchemy label usage
foobar = Foo.bar.label("foobar")
session.query(foobar).filter(foobar &gt; 10).all()

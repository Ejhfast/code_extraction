# Python (Enthought) Tuple / List Trait: how to access a specific element?
tuple = Tuple(blah)
t0 = Property(depends_on="tuple", fget=lambda self: self.tuple[0])

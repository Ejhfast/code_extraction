# How to properly use unit-testing's assertRaises() with NoneType objects?
with self.assertRaises(TypeError):
    self.testListNone[:1]

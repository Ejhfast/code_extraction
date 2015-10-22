# Django test cases for model methods that returns nothing
def test_model_method(self)
    self.instance_object.model_method()
    self.assertEqual(self.instance_object.field1, EXPECTED_FIELD1_VALUE)

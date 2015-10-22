# Adding a value to an Object retrieved via a QuerySet
object_instance = Object.objects.get(pk=pk)
object_instance.special_value = SomeBusinessLogic(data_to_aggregate)

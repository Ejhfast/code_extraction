# Python list comprehension on class
[some_function() if foo.bar else some_other_function()
         for foo in foos if not setattr(foo, 'added',  "I was added in iteration")]

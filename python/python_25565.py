# Mocking out a function on a repeated call with Python mock
copy_of_foo = foo
with patch('...foo') as foo_mock:
   copy_of_foo(args...)

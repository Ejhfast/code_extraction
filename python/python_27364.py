# Using Elixir, erlport with Python 2.7.9, receiving an arity error
{:ok, pp} = :python.start_link()
:python.call(pp, :sys, String.to_atom("version.__str__"), [])

# What parameters can Python pydoc.render_doc() take?
data = "D\x08DA\x08AT\x08TA\x08A\n" #  DATA bigsection header from pydoc
pydoc.render_doc(module).replace(data, '')

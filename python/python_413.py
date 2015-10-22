# How to I get scons to invoke an external script?
env.Command ('document.tex', '', 'python table_generator.py')
env.PDF ('document.pdf', 'document.tex')

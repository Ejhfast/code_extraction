# The ${'foo %(a)s bar %(b)s' % {'a': '1', 'b': '2'}} syntax doesn't work in a Mako template
from mako.template import Template

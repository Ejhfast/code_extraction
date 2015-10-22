# Dealing with timeseries gaps in Chaco
from enthought.chaco.scales.formatters import TimeFormatter
TimeFormatter._formats['days'] = ('%d/%m', '%d%a',)

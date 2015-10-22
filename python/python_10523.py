# Reportlab platypus - disable table splitting
from reportlab.platypus.flowables import KeepTogether
t = Table(tableData)
self.elements[name] = KeepTogether(t)

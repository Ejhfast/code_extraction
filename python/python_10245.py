# PyQt - defining signals for multiple objects in loops
import functools
slot = functools.partial( self.checkState, self.fieldList["valueField" + str(i)] )
self.fieldList["valueField" + str(i)].cursorPositionChanged.connect( slot )

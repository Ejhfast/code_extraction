# Formatting Dictionary Within Object in Python
def __repr__(self):
        return "Rxns catalyzed: %s, Specificity: %s \n" %(self._rxns_cat, ['%.3f' % spec for spec in self._specif])

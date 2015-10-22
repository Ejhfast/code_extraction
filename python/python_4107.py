# Python: How to obtain an instance's name at runtime?
for name, obj in self.__dict__.iteritems():
    if isinstance(obj, QtCore.QObject) and not obj.objectName(): # QObject without a name
        obj.setObjectName(name)

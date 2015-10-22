# How to create objects on the fly in python?
testobj = type('testclass', (object,),
                 {'test':[a1,a2,b2], 'test2':'something else', 'test3':1})()

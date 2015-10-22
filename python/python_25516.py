# Variable variables for use in Element Tree Python
data = dict()
for idx, num in enumerate(someList):
    data['record{}'.format(idx)] = SubElement(records, 'record')

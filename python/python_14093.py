# How can I find a element that has a particular name attribute using ElementTree in Python
for name in namelist:
    firstname = library.find('.//firstname[@name="{}"]'.format(name))

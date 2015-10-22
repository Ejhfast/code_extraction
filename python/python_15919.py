# Python xml : list all elements in item
def process_element(catalog, *args, **kwargs):
    for child in catalog.getchildren():
        print(child.text)

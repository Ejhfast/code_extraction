# How to read an xml file from a folder with python?
etree = ET.parse(filename)
root = etree.getroot()
doc_df = pd.DataFrame(list(iter_docs(root)))

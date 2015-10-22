# When using lxml, can the XML be rendered without namespace attributes?
objectify.deannotate(root, xsi_nil=True)
etree.cleanup_namespaces(root)

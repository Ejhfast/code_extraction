# NLTK 3 POS_TAG throws UnicodeDecodeError
resource_val = pickle.load(opened_resource) #old
resource_val = pickle.load(opened_resource, encoding='iso-8859-1') #new

# Is there anyway to get maximum value in a column using mongoengine?
MyDocument.object().order_by("-max_column").limit(-1).first()

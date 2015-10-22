# Using sqlalchemy.sql.functions.char_length as a filter condition
from sqlalchemy import func
Document.query.filter(func.char_length(Document.doc_number)==5).all()

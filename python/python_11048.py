# How can I avoid multiple loops to get the sorting I require in this sqlalchemy query?
query(Article).filter(Article.focusid.in_(topic_ids)).order_by(desc(Article.datepublished)).limit(10)

# SQLAlchemy - using column in LIKE
session.query(x).join(y).filter("y.info LIKE '%#'||x.name||'#%'").all()

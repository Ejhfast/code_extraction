# How to filter columns in two tables with many-to-many relation?
channels = session.query(Channel).options(eagerload("items")).filter(Channel.items.type == "jpg").all()

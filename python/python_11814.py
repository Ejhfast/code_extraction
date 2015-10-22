# SQLAlchemy: Check if object is already present in table
if session.query(Item.id).filter(Item.email==newItem.email,
                                 Item.type==newItem.type).count() &gt; 0:
    // item exists

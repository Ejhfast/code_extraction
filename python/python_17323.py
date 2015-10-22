# SQLAlchemy foreign key filtering, using a different field than the foreign key field
session.query(SEC_RSS_Model).join(SEC_RSSL_Model.CIK_Table).filter(CIK_Model.ticker == 'YHOO')

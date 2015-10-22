# How do I correct this sqlalchemy.exc.NoForeignKeysError?
CountyCode = Column('CountyCode', String, ForeignKey('tblCounty.CountyCode'))

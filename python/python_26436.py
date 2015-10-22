# Generated queries contain redundant products?
tablebs = relationship('TableB', secondary=TableA2TableB, backref='tableas', lazy="dynamic")

# SQLAlchemy Inserting into Existing Table, default item value for columns unspecified in Model
class MyModel(Base):
    foo = sa.Column(sa.String, default='bar')

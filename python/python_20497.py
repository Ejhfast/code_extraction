# SQLAlchemy: how to perform regexp_replace on column values
@hybrid_property
def original_brand_id(self):
    return cast(func.regexp_replace(self.page_title, '.*::: ',''), Numeric)

# InvalidRequestError: Ambiguous column name '***' in result set, while the request is valid to mysqldb?
fa = aliased(FoodCategory)
s.query(Food, fa).filter(Food.category_id == fa.id).all()

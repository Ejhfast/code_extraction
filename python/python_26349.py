# Grouping and auto incrementing group id in pandas
trades = pd.DataFrame({"Qty":[-25,0,25,50,75,0,25,0,-25,0,-25,-50,0,-25,50,0]})
trades["group"] = (trades.Qty == 0).shift(1).fillna(0).cumsum()

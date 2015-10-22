# python statsmodels: "params" parameter for predict function of arima models
model = sm.tsa.ARMA(y, (2, 2))
results = model.fit()
results.predict()

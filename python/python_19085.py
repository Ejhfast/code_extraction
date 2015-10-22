# Standard errors for multivariate regression coefficients
MSE = np.mean((y - clf.predict(TST).T)**2)
var_est = MSE * np.diag(np.linalg.pinv(np.dot(TST.T,TST)))
SE_est = np.sqrt(var_est)

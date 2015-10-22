# Linear Regression\Gradient Descent python implementation
theta[0] = theta[0] - alpha*1/m*sum([((theta[0]+theta[1]*xi) - yi)**2 for (xi,yi) in zip(x,y)])

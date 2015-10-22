# Pyro4, serve object with constructor parameters. how?
psf = Pyro4.Proxy("PYRONAME:MyApp.Factories.ProductFactory")
product = psf.GetProductOnButton(buttonNoPressed, parentProductId)

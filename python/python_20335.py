# Generating perfect random gaussian numbers
x = np.random.normal(0, 1, size=660)
x = (x - x.mean()) / x.std()

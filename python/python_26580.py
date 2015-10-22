# Float and lambda - getting Type Error, a float is required
lambda i: datetime.fromtimestamp(float(i)).strftime("%H:%M")

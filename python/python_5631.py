# Passing numpy arrays to Java using Jpype
values = valBD.ReadAsArray()
JArray(float, values.ndim)(values.tolist())

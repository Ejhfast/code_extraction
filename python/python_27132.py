# How to access decoded JSON values in .txt file
data2 = jsonpickle.decode(whatever)
data2["Metadata"]["dateAndTime"] = "Whatever"
data2 = jsonpickle.encode(data2)

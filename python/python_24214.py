# Delete every non utf-8 symbols froms string
line=line.encode('utf-8').decode('utf-8','ignore').encode("utf-8")

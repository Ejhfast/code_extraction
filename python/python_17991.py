# naming txt output files python
with open("outputHorizontal.{0}.txt".format(lat), 'w') as file:
    for item in I_list:
        file.write("{}\n".format(item))

# How to write a data to a text file in python?
file = open('filename', 'w');
file.write(data.to_string());    // if data is a pandas.DataFrame object
file.close();

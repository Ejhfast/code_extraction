# By df.to_csv() I am writing data in a file, but I want to add some other data to the same file so I do not want the file to lose the previous data
df.to_csv( *whatever arguments you already had*, mode = 'a')

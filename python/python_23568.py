# Selective printing of rows and columns of csv file in python pandas
df=pandas.read_csv('myfile.csv')   #parse CSV
posts=df[df['post']=='Hi guys']    #Get entries where post is 'Hi Guys'
print posts.comment_by             #show comment user

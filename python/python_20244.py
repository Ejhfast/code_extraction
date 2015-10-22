# Python Get Random Choice From Text File Then Repeat That Choice
mychoice = random.choice(list(open('data_files/script_only_files/titles.csv')))
mytag = '&lt;p&gt;&lt;a href="/' + mychoice.replace(" ", "-").replace("---", "-").replace("\n", "").lower() + '/"&gt;' + mychoice.replace("\n", "") + '&lt;/a&gt;&lt;/p&gt;'

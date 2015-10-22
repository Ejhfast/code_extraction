# Retrieving all "Yahoo Answers" Questions that contain a certain word . Issue with rate limiting
first_50 = app.questionSearch({'query':'tornado', 'start' : 0, 'results' : 50})
next_50 = app.questionSearch({'query':'tornado', 'start' : 50, 'results' : 50})

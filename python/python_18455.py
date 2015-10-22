# Populate a SQL table column based on other values in table
UPDATE TwTbl
  SET LenTweet = length(text)

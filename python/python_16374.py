# python StringBuilder for MySQL query execution
weekNum = "week" + str(i)               #i is either 2, 3, 4, 5
query = "select {0} from golden_table where nGram = %s and hash_tag = %s".format(weekNum)
cur.execute(query, (tup[0], tup[1]))

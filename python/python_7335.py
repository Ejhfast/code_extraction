# Trying to insert variables from two lists into strings - how do I do it?
['&lt;option value="id=%s+%s"&gt;%s - %s&lt;/option&gt;' % (x, y, x, y) for x, y in zip(numlist, numlist2)]

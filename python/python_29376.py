# How to loop over two iterables at once, insert into mysql by python like this?
to_insert = zip(item['link'], item['title'])
for link, title in to_insert:
    xxx.excute(sql % (link, title))

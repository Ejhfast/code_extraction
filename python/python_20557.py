# Extracting frequency from list
title_count = Counter(titles).most_common()
for name,count in title_count:
    print('{} was found {} times'.format(name, count))

# How to Beautiful Soup (bs4) match just one, and only one, css class
for item in soup.find_all('div',class_="ad_item"):
     if len(item["class"]) != 1:
         continue;

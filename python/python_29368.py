# Increment every 33 line of 6 column by 1
awk '!(NR%33){$6+=++p} 1'

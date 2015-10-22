# Is there a method of getting the number of files in git repository with new/modified/deleted status?
git status --porcelain | cut -c 2 | sort | uniq -c

# how can i convert a tuple into string
| | ${str}= | Catenate | @{recordList} |
| | Append to file | /tmp/junk.txt | ${str}

# Unable search names which contain three 7s in random order by AWK/Python/Bash
printf '%s\n' *|awk -F7 NF==4

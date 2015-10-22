# How do I run a script on friday, once every two weeks?
0 7 * * 5 sh -c " if [ $(expr $(expr $(date +\%s) \/ 604800) \% 2) -eq 0 ]; then command; fi "

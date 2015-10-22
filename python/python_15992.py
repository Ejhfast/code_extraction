# Decode JSON in Bash using python mjson.tool
$ echo '{"first_key": "value", "second_key": "value2"}' | python -c 'import sys, json; print json.load(sys.stdin)[sys.argv[1]]' first_key
value

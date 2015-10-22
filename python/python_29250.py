# How to parse parameter's name from JSON with python
echo '{"710":{"sysKey":"ENTER"},"230":{"sysKey":"DELETE"},"804":{"sysKey":"ADD"}}' | python -c 'import json,sys;obj=json.load(sys.stdin);obj=dict((z,x) for x, y in obj.items() for z in y.values());print obj["DELETE"];'

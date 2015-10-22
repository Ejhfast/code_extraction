# Replace all quotes in a string with escaped quotes?
import json
string = 'This sentence has some "quotes" in it\n'
json.dumps(string) #gives you '"This sentence has some \\"quotes\\" in it\\n"'

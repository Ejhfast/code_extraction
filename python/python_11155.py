# Can't write long JSON output to text file
with open('C:/Comparison.txt', 'w') as f:
  json.dump(full_json, f)

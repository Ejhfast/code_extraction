# How can i print columns in same rows with different 'codes' using csv python
for row in rows:
        writer.writerow([row.get("one", ""), row.get("two", "")])

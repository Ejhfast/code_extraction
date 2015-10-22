# Extract data from a website's list, without superfluous tags
definitions = soup('ul')[0].findAll(text=True)

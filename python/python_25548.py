# Regex separate urls in text that has no separators
&gt;&gt;&gt; s = "https://00e9e64bac25fa94607-apidata.googleusercontent.com/download/redacted?qk=AD5uMEnaGx-JIkLyJmEF7IjjU8bQfv_hZTkH_KOeaGZySsQCmdSPZEPHHAzUaUkcDAOZghttps://console.developers.google.com/project/reducted/?authuser=1\n"
&gt;&gt;&gt; re.findall(r'https?://.*?(?=https?://|$|\s)', s)
['https://00e9e64bac25fa94607-apidata.googleusercontent.com/download/redacted?qk=AD5uMEnaGx-JIkLyJmEF7IjjU8bQfv_hZTkH_KOeaGZySsQCmdSPZEPHHAzUaUkcDAOZg', 'https://console.developers.google.com/project/reducted/?authuser=1']

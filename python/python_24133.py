# Manipulating BeautifulSoup's ResultSet list object
for state in state_list:
    print state['value'].split(".")[0], state.text

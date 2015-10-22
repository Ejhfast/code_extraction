# Beautifulsoup: Retrieve specific value in table
p = soup.find(text="Annual Report Expense Ratio (net):").parent.next_sibling.string

# Google Books API - How do I separate Book from Book Edition?
entry = self.service.get_by_google_id("XV0NAQAAIAAJ")
print entry.dc_title[0].text
print entry.date.text

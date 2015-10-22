# Removing ListItemButtons from kivy adapter widget
def clear_locations(self):
    del self.search_results.adapter.data[:]

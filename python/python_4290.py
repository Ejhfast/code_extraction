# How to ensure list contains unique elements?
def addToList(self, str_to_add):
    if str_to_add not in self.list_of_strings:
        self.list_of_strings.append(str_to_add)

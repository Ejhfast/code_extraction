# Python - ObjectListView Filter
def filter_view(self):
    self.SetFilter(olv.Filter.Predicate(self.filter_me))
    self.RepopulateList()

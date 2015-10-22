# How can I get right-click context menus for clicks in QTableView header?
headers = self.tv.horizontalHeader()
headers.setContextMenuPolicy(Qt.CustomContextMenu)
headers.customContextMenuRequested.connect(self.header_popup)

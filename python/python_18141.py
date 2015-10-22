# How to get Chrome's active_tab's url by calling Python's app script?
url = appscript.app("Google Chrome").windows[1].get.tabs[dt.windows[1].get.active_tab_index.get].get.URL.get

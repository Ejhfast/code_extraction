# Python tk scrollbar behavior (Windows to blame?)
my_listbox.configure(yscrollcommand=my_scrollbar.set)
my_scrollbar.configure(command=my_listbox.yview)

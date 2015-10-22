# Updating Tkinter listbox without quitting and re-entering?
listbox.delete(0, END)
for i in range(len(new_list)):
    listbox.insert(END,new_list[i][0])

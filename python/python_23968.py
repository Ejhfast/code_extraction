# Assign fixed number of variables to elements in variable length list
morning_entry,morning_leave,afternoon_entry,afternoon_leave=(timestamps+[None]*4)[:4]

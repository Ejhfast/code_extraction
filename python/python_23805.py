# Understanding the logic of Tkinter mainloop() and why variables are not reassigned their original values?
while (the_main_window_hasnt_been_destroyed):
    event=event_queue.pop()
    event.handle()

# Tkinter one button multiple commands
def run_all(self):
    thread.start_new_thread(self.telnetcap, ())
    thread.start_new_thread(self.get_info, ())

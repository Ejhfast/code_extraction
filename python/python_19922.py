# Simultaneously call functions with different parametrs in Python
import threading
my_thread = threading.Thread(target=your_function, args=(), kwargs={})  # This can go inside a loop, providing different args each time.
my_thread.start()

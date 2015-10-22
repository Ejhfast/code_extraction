# Send mails async in web.py
import threading
threading.Thread(target=sending_email).start()

# Writing to the windows logs in Python
import win32evtlogutil
win32evtlogutil.ReportEvent(ApplicationName, EventID, EventCategory,
          EventType, Inserts, Data, SID)

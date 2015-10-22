# Python Script: Print new line each time to shell rather than update existing line
def report_progress(self, percent_str, data_len_str, speed_str, eta_str):
    """Report download progress."""
    print u'[download] %s of %s at %s ETA %s' % (percent_str, data_len_str, speed_str, eta_str)

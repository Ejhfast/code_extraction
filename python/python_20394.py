# How to refresh the page in Mechanize?
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

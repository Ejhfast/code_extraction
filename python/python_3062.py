# how do i get python's mechanize to stop following meta refresh redirects?
import mechanize
browser = mechanize.Browser()
browser.set_handle_refresh(False)

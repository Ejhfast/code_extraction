# splinter - strange ElementNotVisible exception for link that is indeed visible in dumped html/screenshot
(Pdb) [link.visible for link in my_browser.find_link_by_partial_href('/mystuff/' + str(important_number))]

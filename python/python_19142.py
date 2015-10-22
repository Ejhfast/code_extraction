# How to easily work with python strings containing both single and double quotes?
r'''\copy (select sr, id, rc AS jql from sr UNION select 'quickfilter', "ID", "QUERY" from "AO_60DB71_QUICKFILTER") TO xxx.csv'''

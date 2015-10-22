# changing type of a entry in dictionary throws error
d = {'today': datetime.today()}
d['today'] = d['today'].strftime(&lt;your format&gt;)

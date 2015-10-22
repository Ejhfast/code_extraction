# Python copying one work sheet to another in excel
ws_temp.Range("A5:AF16").Copy(ws_pwr.Range("A%s:AF%s" % (chart_first_row, chart_last_row)))

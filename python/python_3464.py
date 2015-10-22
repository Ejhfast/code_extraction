# Python Visual Basic's CDate equivalent
rpt.ParameterFields.GetItemByName("RowDate").AddCurrentValue(datetime.datetime.strptime('2010-03-19', "%Y-%m-%d").date())

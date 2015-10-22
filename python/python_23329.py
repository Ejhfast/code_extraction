# How do I assign variables within WMI calls?
wmi_sql = wmi.WMI(SQLServer_raw, user="%s\\%s" % (sql_domain, sql_user),
    password=sql_pass)

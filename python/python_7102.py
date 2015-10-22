# Best way to access Firebird DB from a remote desktop.
Import kinterbasdb as k
k.init(type_conv = 300) #
con = k.connect(dsn='127.0.0.1:c:\\db\\test.fdb', user='sysdba', password='masterkey', charset='YOUR_CHARSET', dialect=3)

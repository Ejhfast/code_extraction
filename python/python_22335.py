# Varialbe expansion in exec in BeanShell
String param="parameter1";
Runtime r = Runtime.getRuntime();
Process p = r.exec("/usr/bin/python /path/script.py " + param);

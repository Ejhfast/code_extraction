# Embedded Python loads module but does not load that module's internal import statements
PyRun_SimpleString("sys.path.append(\"&lt;&lt;path&gt;&gt;\")");

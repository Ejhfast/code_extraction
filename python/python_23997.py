# WSadmin TypeError: sequence subscript must be integer or slice using AdminConfig.modify
AdminConfig.modify(connectionPoolId, [["maxConnections", databaseMaxConnections], ["minConnections", databaseMinConnections], ["connectionTimeout", databaseconnTimeout], ["reapTime", databasereapTime], ["unusedTimeout", databaseunusedTimeout], ["agedTimeout", databaseagedTimeout]])

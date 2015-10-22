# How to connect to a mongoDB
database = motor.MotorClient("mongodb://&lt;dbuser&gt;:&lt;dbpassword&gt;@ds047057.mongolab.com:47057/myDatabase").open_sync().myDatabase

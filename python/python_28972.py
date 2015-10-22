# Python Code for Bulk Insert into SQL Server 2014 DateTime format
set dateformat mdy;
bulk insert tbl from 'c:\users\...\tbl.csv' with (fieldterminator = ',', firstrow = 2);

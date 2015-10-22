# Connecting to database using SQLAlchemy
Changed in version 1.0.0: Hostname-based PyODBC connections now require the
SQL Server driver name specified explicitly. SQLAlchemy cannot choose an
optimal default here as it varies based on platform and installed drivers.

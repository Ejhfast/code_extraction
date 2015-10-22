# Python/MySQL - LOAD DATA LOCAL INFILE
from mysql.connector.constants import ClientFlag
conn = mysql.connector.connect(...., client_flags=[ClientFlag.LOCAL_FILES])

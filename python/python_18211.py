# Python os.system launch exe with quotes and dash arguments
import subprocess
subprocess.call(['c://Program Files//SQL Anywhere 11//Bin32//dbbackup.exe','-c',
'"DSN=demo2suite;UID=dba;PWD=sql"', '-y','"D://Databases//AMOS2//LIVE//LIVE_BCK"'])

# How can I start a query in PostgreSQL, then detach the initiating program (e.g. python) so it can be closed, leaving the query to run for days
import subprocess
cmd = ['psql', '-d', 'test', '-U', 'postgres', '-f', 'test_points.pgsql']
subprocess.Popen(cmd)  # will run in the background if the output is not used in the rest of the script

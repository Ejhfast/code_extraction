# Python commands.getstatusoutput() returning 0 even though the command failed
"(rc, op) = commands.getstatusoutput("source /source ; ontape -v -s -L 0 -t STDIO | /bin/gzip ; exit ${PIPESTATUS[0]} &gt; /backup/ontape_backup.gz")"

# I need to run a python script from php
$script = 'software/qiime-1.4.0-release/bin/check_id_map.py -m /home/qiime/sample/Fasting_Map.txt -o /home/qiime/sample/mapping_output -v';
$a = exec($script);

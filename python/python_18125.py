# How to convert datetime string to UTC to plot points on Highcharts
&gt;&gt;&gt; int(datetime.datetime.strptime("2013-11-07 00:10:27", "%Y-%m-%d %H:%M:%S").strftime('%s')) * 1000
1383811827000

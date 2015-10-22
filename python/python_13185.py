# what is a good way to connect to elastic beanstalk in boto when programmatically setting a region?
regionInfo = boto.regioninfo.RegionInfo(None, 'us-west-1', 'elasticbeanstalk.us-west-1.amazonaws.com')
beanstalk = boto.connect_beanstalk(region=regionInfo)
mt.describe_applications()

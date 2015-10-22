# Performing regex Queries with in caluse with django and mongoengine
Job.objects(__raw__={'attributes.Skills.Skill' : {'$in' : [/.*java.*/i]}})  #ignoring sql for now
Job.objects(__raw__={'attributes.Skills.Skill' : {'$in' : ['sql',re.compile('.*java.*', re.IGNORECASE)]}})

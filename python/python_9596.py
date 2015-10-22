# How to create numbered changelist using P4Python?
changespec = P4.fetch_change()
changespec[ "Description" ] = "placeholder"
P4.save_change( changespec )

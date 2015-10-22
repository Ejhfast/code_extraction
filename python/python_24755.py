# Show viewMap until user close it
mapIntent = droid.makeIntent("android.intent.action.PACKAGE_FIRST_LAUNCH", str(droid.viewMap(dic["latitude"]+","+dic["longitude"])))
droid.startActivityIntent(mapIntent, True)

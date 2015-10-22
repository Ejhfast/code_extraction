# Parse date and time from string with time zone using Arrow
arrow.get(s, 'YYYY/M/D HH:mm:ss').replace(tzinfo=dateutil.tz.gettz(tz))

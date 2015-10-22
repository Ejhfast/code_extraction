# Convert int(round(time.time())) to C#
TimeSpan t = (DateTime.UtcNow - new DateTime(1970, 1, 1));
int timestamp  = (int) t.TotalSeconds;

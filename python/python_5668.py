# Clutter - run method at marker?
g_signal_connect (timeline, "marker-reached::my-marker",
                  G_CALLBACK (on_my_marker_reached),
                  NULL);

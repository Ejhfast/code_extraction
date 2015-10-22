# gtk.gdk.color_parse() equivalent in vala
Gdk.Color fuchsia;
if (!Gdk.Color.parse("fuchsia", out fuchsia))
    print("There was an error parsing, I must have spelled fuchsia wrong");

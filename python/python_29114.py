# Adding second x_axis writes over title
title = fig.set_title("Flying monkey density")
title_xy = title.get_position()
title.set_position([title_xy[0], title_xy[1]*1.05])

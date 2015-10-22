# How to calculate the number of box according to their position?
relx, rely = ev.pos[x] - mx, ev.pos[y] - my
number = rely//boxsize*numboxsx + relx//boxsize

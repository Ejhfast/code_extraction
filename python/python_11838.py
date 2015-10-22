# integrate.odeint gives two very different answers when it shouldn't
y2 = integrate.odeint(eqexec2,inits, trange, full_output=0, printmessg=1,hmax=1.0)

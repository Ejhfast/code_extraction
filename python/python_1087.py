# Return value while using cProfile
prof = cProfile.Profile()
retval = prof.runcall(self.method_actual, *args, **kwargs)
prof.dump_stats(datafn)

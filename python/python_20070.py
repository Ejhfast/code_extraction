# unable to release GIL with Cython when using callback-based C libraries
thread = threading.Thread(target=win.player.get_midi_in, args=(test,))

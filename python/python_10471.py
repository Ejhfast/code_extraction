# subprocess grab stdout of airodump-ng
o_airodump, unused_stderr = airodump.communicate(timeout=15)
airodump.kill()

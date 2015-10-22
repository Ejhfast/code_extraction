# Why does the terminal search the working directory for files that an executing file is searching for?
import os
hit = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "hit.wav"))

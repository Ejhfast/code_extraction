# PyQT phonon volume slider? how to connect it on my phonon player
#self.audioOutput = Phonon.AudioOutput(Phonon.VideoCategory, self)
#Phonon.createPath(self.ui.videoPlayer.mediaObject(), self.audioOutput)
self.ui.volumeSlider.setAudioOutput(self.ui.videoPlayer.audioOutput())

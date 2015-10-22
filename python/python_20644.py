# one list a percentage of another
plt.plot([percentage(tts, vol) for vol, tts in zip(Volume, TTS)])

# Text to Speech Library for Python using Windows 8.1 (SAPI)
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it works!")

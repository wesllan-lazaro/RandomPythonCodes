import numpy
import soundfile
import sounddevice  


a, b  = soundfile.read("End Of Valor - Density & Time.mp3")

sounddevice.play(a, b)

sounddevice.wait()
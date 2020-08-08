import sounddevice as sd
from aubio import source, pitch
from itertools import zip_longest
import numpy as np

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

duration = 5  # seconds
print('Starting record')
fs= 44100 
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
#sd.default.device = 10
sd.wait()
print(myrecording)
#sd.play(myrecording, fs, blocking=True)
#sd.wait()
print(sd.query_devices())
pitch_fn = pitch("yin", 4096, 512, 44100)
myrecording = myrecording.ravel()
for chunk in grouper(myrecording, 512, 0.0):
    pitch_fn(np.array(chunk, dtype=np.float32))
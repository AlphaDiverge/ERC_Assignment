I made the FFT using Python numpy, scipy and matplotlib.
I could not complete this work fully but still am submitting what i did till now. I faced a lot of time constraints due to my lab endsems.
I could only write the FFT part and the demodulation part and not the cleaning part.
I got time to learn the FFT part fully and coded it on my own whereas the demodulation i did copy some bits of code as i couldnt get the time to learn it fully.

This is the code i wrote:

import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

sample_rate, data = wavfile.read('C:/Users/soura/Downloads/signal_modulated_noisy_audio.wav')

data = data.astype(np.float32) / np.max(np.abs(data))

N = len(data)
yf = fft(data)
xf = fftfreq(N, 1 / sample_rate)

plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.xlabel("Frequency in Hz")
plt.ylabel("Magnitude of each Frequency")
plt.title("FFT of Input Signal")
plt.grid()
plt.show()

envelope = np.abs(data)
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
b, a = butter_lowpass(4000, sample_rate)
demodulated = lfilter(b, a, envelope)
demodulated = demodulated / np.max(np.abs(demodulated))

sd.play(demodulated, sample_rate)
wavfile.write('C:/Users/soura/Downloads/Final_made.wav', sample_rate, demodulated)
sd.wait()

![Figure_1](https://github.com/user-attachments/assets/fbf73d54-b15c-4f7c-91e0-ee0f8de51539)

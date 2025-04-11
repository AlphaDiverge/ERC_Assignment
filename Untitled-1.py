import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

sample_rate, data = wavfile.read('C:/Users/soura/Downloads/signal_modulated_noisy_audio.wav')

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
wavfile.write('C:/Users/soura/Downloads/Final.wav', sample_rate, demodulated)
sd.wait()
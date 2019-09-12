'''
Created on Sep 12, 2019

@author: charlie_tharas
'''

from playsound import playsound
from scipy.fftpack import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import os
import time

# initial fft algorithm
rate, data = wavfile.read("C:/Users/charl_itcmbk/eclipse-workspace-python/Fourier/res/allthistime_20ms.wav")
print("Wave file load successful.")
fft_out = fft(data)
print("FFT conversion successful. Preparing to plot.")

# initial plotting
# plt.plot(data, np.abs(fft_out))
# plt.show()
print("Plotting successful.")

# so the sound goes along
# playsound('allthistime.mp3')

# going through fft in cut directory
for file in os.listdir("C:/Users/charl_itcmbk/eclipse-workspace-python/Fourier/res/cut/"):
    filename = os.fsdecode(file)
    print("Check " + filename)
    if filename[len(filename)-3:len(filename)] == "wav":
        readfilepath = "C:/Users/charl_itcmbk/eclipse-workspace-python/Fourier/res/cut/" + filename
        rate, data = wavfile.read(readfilepath)
        fft_out = fft(data)
        plt.plot(data, np.abs(fft_out))
        plt.show(block=False)
        plt.pause(0.01)
        plt.clf()
    
plt.show()
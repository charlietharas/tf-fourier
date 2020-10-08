'''
Created on Sep 12, 2019
@author: charlie_tharas
'''

import os
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import rfft
from scipy.io import wavfile
from numpy.core._multiarray_umath import arange
import numpy as np

def visualize():
    # going through fft in cut directory
    for file in os.listdir("../res/cut/"):
        filename = os.fsdecode(file)
        print("Check " + filename)
        if filename[len(filename)-3:len(filename)] == "wav":
            readfilepath = "../res/cut/" + filename
            loadFFTGraph(readfilepath)
            
    plt.show()

# Note that filepaths vary off of OS & Location (see filepath list doc)
def loadFFTGraph(filepath):
    rate, data = wavfile.read(filepath)
    
    channel = data.T[0] # grab 1st channel
    normalize = [(i/2**8.)*2-1 for i in channel] # normalize track
    fft_data = rfft(normalize) # perform fourier transform
    fft_out = len(fft_data)/2 # half of fft (signal symmetry)
    fft_out = int(fft_out) # normalize integer function for plot
    
    a = arange(len(data))
    b = len(data)/rate # length of wav file
    frqLabel = a/b # unknown application
    
    plt.clf() # facilitates animation
    plt.plot(abs(fft_data[:(fft_out-1)]),'r')
    plt.show(block=False) # disable for constant visualization
    plt.pause(0.05) # not advisory to adjust interval from 0.05
    
def vectorizedEqualityRating(wav1, wav2):
    # how to vectorize?
    # see notes in official folder 10-8-20
    rate_1, data_wav_1 = wavfile.read(wav1)
    rate_2, data_wav_2 = wavfile.read(wav2)
    for j in range(1, int(data_wav_1.shape[0]/rate_1)):
        for j in range(1, int(data_wav_2.shape[0]/rate_2)):
            # how to grab a slice from the wav file??
            continue
    
def amplitudePlot(filepath):
    # TODO
    rate, data = wavfile.read(filepath)
    
# Pseudocode (Temp)
# r = sum(j1=1:len(w1)/int_size)(f(w1[j1])/f(w1[j1-1])-f(w2[j2])/f(w2[j2-1]))
    
loadFFTGraph("../res/allthistime_1s.wav")
    
# plotting amplitude
test_rate, test_data = wavfile.read("../res/allthistime.wav")
print(test_data.shape[0]/test_rate)
time = np.linspace(0., test_data.shape[0]/test_rate, test_data.shape[0])
plt.plot(time, test_data[:, 0], label="Left channel")
plt.plot(time, test_data[:, 1], label="Right channel")
#plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

visualize()


'''
Created on Sep 12, 2019
@author: charlie_tharas
'''

import os
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from numpy.core._multiarray_umath import arange

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
    fft_data = fft(normalize) # perform fourier transform
    fft_out = len(fft_data)/2 # half of fft (signal symmetry)
    fft_out = int(fft_out) # normalize integer function for plot
    
    a = arange(len(data))
    b = len(data)/rate
    frqLabel = a/b # unknown application
    
    plt.plot(abs(fft_data[:(fft_out-1)]),'r')
    plt.show(block=False) # disable for constant visualization
    plt.pause(1)
    
loadFFTGraph("../res/allthistime_20ms.wav")
visualize()

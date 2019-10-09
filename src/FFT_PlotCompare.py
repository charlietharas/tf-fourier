'''
Created on Sep 12, 2019
@author: charlie_tharas
'''

import os
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from numpy.core._multiarray_umath import arange
from pydub import AudioSegment
import librosa

def visualize():
    activeFile = AudioSegment.from_wav("../res/active/active.wav") # load active file
    activeFileLength = librosa.get_duration(filename="../res/active/active.wav") # get duration
    for i in range(0, int(activeFileLength*1000)): # iterates over the duration of the file in ms
        activeFileCut = activeFile[i:i+10] # segments the file into next section: (Xms ahead)
        activeFileCut.export("../res/active/active-cut.wav", format="wav") # exports new file 
        loadFFTGraph("../res/active/active-cut.wav", False, 0.01) # reads exported file and plots every 10 milliseconds
        i+= 10 # reads 10ms chunks
    
# Single File Display
def loadFFTGraph(filepath, blockValue, waitTime):
    
    rate, data = wavfile.read(filepath)
    
    channel = data.T[0] # grab 1st channel
    normalize = [(i/2**8.)*2-1 for i in channel] # normalize track
    fft_data = fft(normalize) # perform fourier transform
    fft_out = len(fft_data)/2 # half of fft (signal symmetry)
    fft_out = int(fft_out) # normalize integer function for plot
    
    channel2 = data.T[1] # grab 1st channel
    normalize2 = [(i/2**8.)*2-1 for i in channel2] # normalize track
    fft_data2 = fft(normalize2) # perform fourier transform
    fft_out2 = len(fft_data)/2 # half of fft (signal symmetry)
    fft_out2 = int(fft_out2) # normalize integer function for plot
    
    a = arange(len(data))
    b = len(data)/rate
    frqLabel = a/b # unknown application-- currently unused
    
    plt.plot(abs(fft_data[:(fft_out-1)]),'r')
    plt.plot(abs(fft_data2[:(fft_out2-1)]),'r')

    plt.xlim(0, 100) # XLIM and YLIM can be changed to better view/visualize/interpret data
    #plt.ylim(0, 6000)
    plt.show(blockValue) # disable for constant visualization
    plt.pause(waitTime) # ms time to plot
    plt.clf()
    
visualize()

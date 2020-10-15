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

# performs simple FFT
# fix normalization? this normalizes for 8-bit files..
def getFFT(rate, data):
    channel = data.T[0]
    normalize = [(i/2**8.)*2-1 for i in channel]
    return fft(normalize)

# returns slice_interval (in s) cut of data
def getCut(data, rate, pos, slice_interval=0.02):
        # print(pos, np.size(data[int(pos*slice_interval*rate):int((pos+1)*slice_interval*rate)])) # debug
        return data[int(pos*slice_interval*rate):int((pos+1)*slice_interval*rate)]

# static fft graph of file            
def loadFFTGraph(filepath):
    rate, data = wavfile.read(filepath)
    
    channel = data.T[0] # grab 1st channel
    bits = 8. # bitrate of track
    normalize = [(i/2**bits)*2-1 for i in channel] # normalize track
    normalize = data.T[0] # debug skip normalization
    fft_data = fft(normalize) # perform fourier transform
    fft_out = len(fft_data)/2 # half of fft (signal symmetry)
    fft_out = int(fft_out) # normalize integer function for plot
    
    a = arange(len(data))
    b = len(data)/rate # length of wav file
    frqLabel = a/b # unknown application
    
    plt.clf() # facilitates animation
    plt.plot(abs(fft_data[:(fft_out-1)]),'r')
    plt.show() # disable for constant visualization
    
# live visualizer at interval cut_size
def visualize(filepath, cut_size=0.02):
    rate, data = wavfile.read(filepath)
    channel = data.T[0]
    normalize = [(i/2**8.)*2-1 for i in channel]
    print("Visualizer preprocessing complete")
    for pos in range (int(len(normalize)/rate/0.02)-1):
        fft_data = rfft(getCut(data, rate, pos, cut_size))
        fft_out = int(len(fft_data))
        plt.clf()
        plt.plot(abs(fft_data[:(fft_out-1)]), 'r')
        plt.show(block=False)
        plt.pause(cut_size)
        if pos % (1/cut_size) == 0:
            print(pos/(1/cut_size), "seconds processed.")
        
    plt.show()
    
# simple amplitude plot
def plotAmplitude(filename):
    test_rate, test_data = wavfile.read(filename)
    print("Got file length (s):", test_data.shape[0]/test_rate)
    time = np.linspace(0., test_data.shape[0]/test_rate, test_data.shape[0])
    plt.plot(time, test_data[:, 0], label="Left channel")
    plt.plot(time, test_data[:, 1], label="Right channel")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()
    
# not working great/at all
def permutatedSimilarityRating(wav1, wav2):
    # how to vectorize?
    # see notes in official folder 10-8-20
    rate_1, data_1 = wavfile.read(wav1)
    data_1 = data_1.T[0]
    rate_2, data_2 = wavfile.read(wav2)
    data_2 = data_2.T[0]
    rating = 0
    j1_max = int((data_1.size/rate_1)/0.02)
    j2_max = int((data_2.size/rate_2)/0.02)
    print("Iterations to perform:", j1_max, j2_max) # debug
    for j1 in range(1, j1_max):
        sel_1 = np.divide(getCut(data_1, rate_1, j1), getCut(data_1, rate_1, j1-1))
        for j2 in range(1, j2_max):
            sel_2 = np.divide(getCut(data_2, rate_2, j2), getCut(data_2, rate_2, j2-1))
            sigmoid_in = np.abs(np.subtract(sel_1, sel_2)) # should i use activation functions?
            rating += 1/(1 + np.exp(-sigmoid_in))[0] # [0] is temporary, better solution needed to return scalar
    
    rating = rating/(j1_max*j2_max) # does averaging need fixing?
    print("rated", rating)
    return rating

# matches difference against live timestamp (poor ubiquitous similarity rating)
def exactSimilarityRating(wav1, wav2):
    rate_1, data_1 = wavfile.read(wav1)
    data_1 = data_1.T[0]
    rate_2, data_2 = wavfile.read(wav2)
    data_2 = data_2.T[0]
    rating = 0
    j1_max = int((data_1.size/rate_1)/0.02)
    j2_max = int((data_2.size/rate_2)/0.02)
    j1_max = min(j1_max, j2_max)
    for j1 in range(1, j1_max-1):
        sel_1 = np.divide(getCut(data_1, rate_1, j1), getCut(data_1, rate_1, j1-1))
        sel_2 = np.divide(getCut(data_2, rate_2, j1), getCut(data_2, rate_2, j1-1))
        # currently no activation function in use
        rating += np.abs(np.subtract(sel_1, sel_2))[0] # [0] is temporary, better solution needed to return scalar
        
    rating = rating/(j1_max)
    print("rated", rating) # closer to 0 is more similar
    return rating
    
exactSimilarityRating("../res/kickdrum.wav", "../res/kickdrum.wav")

plotAmplitude("../res/kickdrum.wav")
loadFFTGraph("../res/kickdrum.wav")
visualize("../res/kickdrum.wav", 0.05)
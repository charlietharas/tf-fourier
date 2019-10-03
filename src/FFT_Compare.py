'''
Created on Sep 12, 2019

@author: charlie_tharas
'''

from playsound import playsound
from scipy.fftpack import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt
import os
from scipy.signal.signaltools import detrend
from numpy.lib.function_base import average
import numpy

# Note that filepaths vary off of OS & Location (see filepath list doc)
def loadFFTGraph(filepath):
    rate, data = wavfile.read(filepath)
    data = detrend(data, 0)
    fft_out = fft(data)
    #plt.plot(numpy.real(fft_out))
    plt.plot(numpy.real(data))
    plt.show()


def playaudio(audiostring):
    playsound(audiostring)


loadFFTGraph("D:/Coding/GitHub/fourier/res/allthistime_20ms.wav")

# COMPARE YIELDS THAT FFT AND ORGIINAL DATA MATCH PERFECTLY

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

print("Plotting successful.")

def loadFFTGraph(filepath, ):
    rate, data = wavfile.read("C:/Users/charl_itcmbk/eclipse-workspace-python/Fourier/res/allthistime_20ms.wav")
    fft_out = fft(data)
    # TODO (see visualize())


def playaudio(audiostring):
    playsound(audiostring)


def visualize():
    # going through fft in cut directory
    for file in os.listdir("C:/Users/charl_itcmbk/eclipse-workspace-python/Fourier/res/cut/"):
        filename = os.fsdecode(file)
        print("Check " + filename)
        if filename[len(filename)-3:len(filename)] == "wav":
            readfilepath = "C:/Users/charl_itcmbk/eclipse-workspace-python/Fourier/res/cut/" + filename
            rate, data = wavfile.read(readfilepath)
            data = detrend(data, 0)
            fft_out = fft(data)
            
            # skip plotting if data contains nothing
            if average(data) != 0:
                plt.plot(fft_out)
                plt.show(block=False)
                plt.xlabel("Frequency (Hz)")
                plt.xlim(500, 1500)
                plt.pause(1)
                plt.clf()
            
    plt.show()
    

visualize()
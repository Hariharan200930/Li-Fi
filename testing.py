import numpy as np

import matplotlib.pyplot as plt
from scipy.io import wavfile


sample_rate = 44100
freq = 2  #herz
length = 1.0

t = np.arange(0,length/freq,1.0/sample_rate)   #1

t = np.arange(0,length,1.0/sample_rate)        #strt,end,divisions
x = np.pi*2*freq*t                             #formula        #2

#to find the no of cycles per herz
#types of signals

sin_square = np.append(-((x/np.pi)%2)+1,np.abs((x/np.pi-0.5)%2-1)*2-1)

signal = np.array(list(sin_square)*(int(freq/2)))

#signal = np.sin(x)                          #sine
#signal = np.abs((x/np.pi-0.5)%2-1)*2-1      #triangle
signal = np.where(x/np.pi % 2 > 1,-1,1)     #square
#signal = -((x/np.pi)%2)+1                   #sawtooth


#signal = np.random.random(int(length*sample_rate))*2.0-1.0      #random noise
#signal = normalization(np.random.randn(int(length*sample_rate)))                #normal noise

plt.plot(range(len(signal)),signal)
plt.show()

signal *= 32767 #1111 1111 1111 1111(binary value) to 65535(decimal value)/2= 32767
signal = np.int16(signal)
wavfile.write("file.wav",sample_rate,signal)
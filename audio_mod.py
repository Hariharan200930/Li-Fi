import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

class ToneGenerator:
    sample_rate = 44100
    def __init__(self):

        self.length = None
        self.freq = None
        self.signal = None
        self.shape = None

    def render(self,length,freq,shape):
        self.length = length
        self.freq = freq
        self.shape = shape
        self.t = np.arange(0, self.length, 1.0 / ToneGenerator.sample_rate)
        x = np.pi * 2 * self.freq * self.t  #t

        if(shape == "sine"):
            self.signal = np.sin(x)
        elif(shape == "triangle"):
            self.signal = np.abs((x/np.pi-0.5)%2-1)*2-1
        elif(shape == "saw"):
            self.signal = -((x/np.pi)%2)+1
        elif(shape == "square"):
            self.signal = np.where(x/np.pi % 2 > 1,-1,1)
        else:
            self.signal = np.random.random(int(self.length * ToneGenerator.sample_rate)) * 2.0 - 1.0

        return  self.signal

    def plot(self):
        plt.plot(self.t, self.signal)
        plt.show()


    def normalization(self,dat):
        min_v = min(dat)
        max_v = max(dat)
        offset = min_v + max_v
        dat = dat+(offset/2)
        dat = np.array([((x - min_v) / (max_v - min_v))for x in dat])*2.0-1
        return dat*((max_v/min_v)*-1)

    @staticmethod
    def write_file(signal,name="file.wav"):
        signal *= 32767  # 1111 1111 1111 1111(binary value) to 65535(decimal value)/2= 32767
        signal = np.int16(signal)
        wavfile.write(name, ToneGenerator.sample_rate, signal)       #self.sample_rate

#sample_rate = 44100
#freq = 200  #herz
#length = 1.0

#t = np.arange(0,length/freq,1.0/sample_rate)   #1

#t = np.arange(0,length,1.0/sample_rate)        #strt,end,divisions
#x = np.pi*2*freq*t                             #formula        #2

#to find the no of cycles per herz
#types of signals

#sin_square = np.append(-((x/np.pi)%2)+1,np.abs((x/np.pi-0.5)%2-1)*2-1)

#signal = np.array(list(sin_square)*(int(freq/2)))

#signal = np.sin(x)                          #sine
#signal = np.abs((x/np.pi-0.5)%2-1)*2-1      #triangle
#signal = np.where(x/np.pi % 2 > 1,-1,1)     #square
#signal = -((x/np.pi)%2)+1                   #sawtooth


#signal = np.random.random(int(length*sample_rate))*2.0-1.0      #random noise
#signal = normalization(np.random.randn(int(length*sample_rate)))                #normal noise

#plt.plot(range(len(signal)),signal)
#plt.show()

#signal *= 32767 #1111 1111 1111 1111(binary value) to 65535(decimal value)/2= 32767
#signal = np.int16(signal)
#wavfile.write("file.wav",sample_rate,signal)

if __name__ =="__main__":
    tone = ToneGenerator()
    freqs = [43,67,86,35,23,45,68,34,84,52,67,35]
    mellody =[]

    for i in range(200):
        mellody += list(tone.render(0.1,freqs[i%len(freqs)]+(i*3),"saw"))

    #print(tone.render(3.0,234,"sawtooth"))

    ToneGenerator.write_file(np.array(mellody))
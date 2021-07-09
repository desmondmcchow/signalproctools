import numpy as np
import matplotlib.pyplot as plt
import math

timestep=1
maxtime=20000
t=np.arange(-maxtime,maxtime,timestep)
pdur=10 # ns

pulsetype=0
#gaussian pulse
if pulsetype==1:
    sigma=pdur/2.3548
    pulse=np.exp(-1*np.power(t,2)/(2*np.power(sigma,2)))

#square pulse
else:
    pulse=np.zeros(t.size)
    for i in range(t.size):
        a = 1
        if abs(t[i]) <= pdur/2:
            pulse[i] = a*1
        else:
            pulse[i] = 0

# pulse repetition
repbool=1

pulsetot=0
if repbool==1: 
    reprate=1 # MHz
    reptime=(1/reprate)*1e3 # in ns
    pulsetemp=0
    maxrep=math.floor(maxtime/reptime)
    for i in range(maxrep):
        pulsepos=np.roll(pulse,(i+1)*int(round(reptime/timestep)))
        pulsepos[t<0]=0
        pulseneg=np.roll(pulse,-(i+1)*int(round(reptime/timestep)))
        pulseneg[t>0]=0
        pulsetemp=pulsetemp+pulsepos+pulseneg
    pulsetot=pulse+pulsetemp
else:
    pulsetot=pulse

plt.figure(1)
plt.subplot(311)
plt.plot(t/1e3,pulsetot,'-b')
plt.xlabel('Time (us)')
plt.xlim(right=2)
plt.xlim(left=-2)
plt.tight_layout()

n=t.size
freq=np.fft.fftfreq(n,d=timestep)
freq=np.fft.fftshift(freq)
sp=np.fft.fft(pulsetot)
sp=np.fft.fftshift(sp)
sp_nu_eval=abs(sp)

plt.subplot(312)
plt.plot(freq*1e3,sp_nu_eval/max(sp_nu_eval),'-b') 
plt.xlabel('Frequency (MHz)')
plt.tight_layout()

plt.subplot(313)
plt.plot(freq*1e3,sp_nu_eval/max(sp_nu_eval),'-b')
plt.xlabel('Frequency (MHz)')
plt.xlim(right=2)
plt.xlim(left=-2)
plt.tight_layout()

plt.savefig("pulsespectrum"+".png", dpi = 300) 
import numpy as np
import matplotlib.pyplot as plt

# https://lpsa.swarthmore.edu/Convolution/Convolution2.html

dt=1e-3
Tmax=5
t=np.arange(0,Tmax,dt)

ft=(t<=1)*1
ht=np.exp(-2*t)

#numerical
yt=np.convolve(ft,ht)*(dt)
tc=np.arange(0,np.size(yt),1)*(dt)

#analytical
Nc=np.size(tc)
yt_an=np.zeros(Nc)
for i in range(Nc):
    if tc[i]<=1:
        yt_an[i]=(1/2)*(1-np.exp(-2*tc[i]))
    elif tc[i]>1:
        yt_an[i]=np.exp(-2*(tc[i]-1))*((1/2)*(1-np.exp(-2)))
            
plt.figure(1)
ax=plt.subplot(111)
ax.plot(tc,yt,'-b')
ax.plot(tc,yt_an,'--r')
plt.xlim([0,5])
plt.ylim([0,0.5])
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift, ifft

def f(t):
    a = 1000
    return np.exp(-a*np.power(t,2))

N=int(np.power(2,12))
Tmax=2
timestep=Tmax/N

t=np.linspace(-(N/2)*timestep, (N/2-1)*timestep, N)

plt.figure(1)
plt.subplot(311)
plt.plot(t,f(t))
plt.xlabel('Time')
plt.ylabel('f(t)')
plt.title('Time domain')

freq = fftfreq(N, timestep)
freq = fftshift(freq)
sp = fft(f(t))
sp = fftshift(sp)
sp = Tmax/N*np.abs(sp)

# analytical http://mathworld.wolfram.com/FourierTransformGaussian.html
def sp_an(freq):
    a = 1000
    return np.sqrt(np.pi/a)*np.exp(-1*np.power(np.pi,2)*np.power(freq,2)/a)

plt.subplot(312)
sp_nu_eval=abs(sp)
sp_an_eval=abs(sp_an(freq))
plt.plot(freq,sp_nu_eval,'-b')
plt.plot(freq,sp_an_eval,'or')
plt.xlabel('Frequency')
plt.ylabel('abs(f(t))')
plt.title('FFT')

finv=ifft(sp)  
finv=fftshift(finv)
finv=finv*N/Tmax #normalization
plt.subplot(313)
plt.plot(t,abs(finv))
plt.xlabel('Time')
plt.ylabel('f(t)')
plt.title('Inverse FFT')
plt.show()  

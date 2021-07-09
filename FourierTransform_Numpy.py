import numpy as np
import matplotlib.pyplot as plt

def f(t):
    a = 1000
    return np.exp(-a*np.power(t,2))

timestep=0.001
Tran=10
t=np.arange(-Tran/2,Tran/2,timestep)

plt.figure(1)
plt.subplot(311)
plt.plot(t,f(t))
plt.xlabel('Time')
plt.ylabel('f(t)')
plt.title('Time domain')

n=t.size
freq=np.fft.fftfreq(n,d=timestep)
freq=np.fft.fftshift(freq)
sp=np.fft.fft(f(t),norm=None)
sp=np.fft.fftshift(sp)
sp=sp*Tran/n #normalization

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

finv=np.fft.ifft(sp,norm=None)  
finv=finv*n/Tran #normalization
plt.subplot(313)
plt.plot(t,abs(finv))
plt.xlabel('Time')
plt.ylabel('f(t)')
plt.title('Inverse FFT')
plt.show()  
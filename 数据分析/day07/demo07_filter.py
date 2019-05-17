# coding=utf-8
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rates,noised_sigs = wf.read('../da_data/noised.wav')
print(sample_rates)
print(noised_sigs.shape)

#整理一组x坐标
times = np.arange(len(noised_sigs))/sample_rates
print(times)
mp.figure("Filter",facecolor='lightgray')
mp.subplot(221)
mp.ylabel("Signal",fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178],noised_sigs[:178],c="dodgerblue",label="Noised")
mp.legend()
#2
freqs=nf.fftfreq(times.size,1/sample_rates)
noised_complex = nf.fft(noised_sigs)
noised_pows = np.abs(noised_complex)
mp.subplot(222)
mp.ylabel("Power",fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.semilogy(freqs[freqs>0],noised_pows[freqs>0],c='orangered',label="Noised")
mp.legend()

#3
fund_freqs=freqs[noised_pows.argmax()]
noised_inds=np.where(freqs !=fund_freqs)
filter_complex = noised_complex.copy()
filter_complex[noised_inds]=0
filter_pows = np.abs(filter_complex)

mp.subplot(224)
mp.ylabel("Power",fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.plot(freqs[freqs>0],filter_pows[freqs>0],c='orangered',label="Filter")
mp.legend()


#4
filter_sigs=nf.ifft(filter_complex).real
mp.subplot(223)
mp.ylabel("Signal",fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178],filter_sigs[:178],c="dodgerblue",label="Filter")
mp.legend()

wf.write('../da_data/out.wav',sample_rates,filter_sigs.astype('int16'))
mp.tight_layout()
mp.show()


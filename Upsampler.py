import matplotlib.pyplot as plt
import numpy as np

input_signal=[1,2,3,4,5]
up_sampler=4

#Upsampled Signal
upsampled_signal=np.zeros(len(input_signal)*up_sampler)
upsampled_signal[::up_sampler]=input_signal

plt.subplot(2,1,1)
plt.stem(input_signal)
plt.title("Input Signal")
plt.xlabel("n")
plt.ylabel("x[n]")

plt.subplot(2,1,2)
plt.stem(upsampled_signal)
plt.title("Upsampler")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.show()
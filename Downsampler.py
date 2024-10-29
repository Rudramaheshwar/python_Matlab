import numpy as np
import matplotlib.pyplot as plt
def downsample(data, factor):
    return np.array(data)[::factor]

input_signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
factor = int(input("Enter Downsampling factor: "))
downsampled_data = downsample(input_signal, factor)
print("Downsampled Data:", downsampled_data)
plt.subplot(2,1,1)
plt.stem(input_signal)

plt.subplot(2,1,2)
plt.stem(downsampled_data)
plt.show()
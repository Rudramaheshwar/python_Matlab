import numpy as np
import matplotlib.pyplot as plt

x=[12,23,43,54,10]
h=[1,2,3,4,5]
l=len(x)+len(h)-1

y=np.zeros(l)
for n in range(l):
	for k in range(len(h)):
		if n-k>=0 and n-k<len(x):
			y[n]+=x[n-k]*h[k]
print(f'Input signal: {x} \n output signal: {y}')
plt.figure(figsize=(10,8))
plt.subplot(3,1,1)
plt.stem(x)
plt.title("Input signal")

plt.subplot(3,1,2)
plt.stem(h)
plt.title("Impulse response")

plt.subplot(3,1,3)
plt.stem(y)
plt.title("Convolution")
plt.tight_layout()
plt.show()

import numpy as np
from matplotlib import pyplot as plt
import random

x=[]
n=int(input("Enter input signal length: "))
for i in range(n):
	x.append(random.randint(1,50))

windows_size=int(input("Enter windows size: "))

y=[]
l=len(x)-windows_size+1
for i in range(l):
	avg=x[i:i+windows_size]
	y.append(abs(sum(avg)/windows_size))

print(x)
print(y)

plt.subplot(2,1,1)
plt.stem(x)
plt.title("Input Signal")

plt.subplot(2,1,2)
plt.stem(y)
plt.title("Moving Average")
plt.show()
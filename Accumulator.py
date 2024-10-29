import random
import numpy as np
import matplotlib.pyplot as plt
x=[]
n=int(input("Enter input signal Length: "))
for i in range(n):
	x.append(random.randint(1,100))

accumulator=np.zeros(len(x))
for i in range(len(x)):
	accumulator[i]=np.sum(x[:i])

print(f"Original Singal: {x}")
print(f"accumulator: {accumulator}")

plt.subplot(2,1,1)
plt.stem(x)
plt.title("Original Signal")
plt.xlabel("n")
plt.ylabel("x[n]")

plt.subplot(2,1,2)
plt.stem(accumulator)
plt.title("Accumlated Signal")
plt.xlabel("n")
plt.ylabel("y[n]")

plt.tight_layout()
plt.show()
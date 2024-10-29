import numpy as np
from matplotlib import pyplot as plt
x=[1,2,3,4]
X=[]
w=np.arange(-1*np.pi,np.pi,0.0001*np.pi)
for i in range (len(w)):
    s=0
    for n in range (0,len(x)) :
        s=s+x[n]*np.exp(-1*1j*w[i]*n)
    X.append(s)
    X[i]=s
plt.title("DTFT")
plt.xlabel("frequency")
plt.ylabel("Magnitude")
plt.plot(w,np.abs(X))
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

data = np.genfromtxt("p04.dat", delimiter="\t")
fit = np.poly1d(np.polyfit(data[:,0], data[:,1], 6))
fitx = np.linspace(data[:,0].min(), data[:,0].max(),100)
fity = fit(fitx)
# print(data)
# print(fitx-fity)

plt.subplot(211)
plt.scatter(data[:,0], data[:,1], label="data")
plt.plot(fitx, fity, label="fit", linestyle="--")
plt.xlabel("X variable (A.U.)")
plt.ylabel("Y variable (A.U.")
plt.legend()

plt.subplot(212)
poli = np.poly1d([4,-4,1,1])
polirange = np.linspace(-10,10,201)
polidata = poli(polirange)
deri = np.polyder(poli)
deridata = deri(polirange)
plt.plot(polirange, polidata, label="poli", color="red")
plt.plot(polirange, deridata, label="deri", color="green")
plt.xlabel("X variable2 (A.U.)")
plt.ylabel("Y variable2 (A.U.")
plt.legend()

textdata = np.zeros((201,2))
textdata[:,0] = polirange
textdata[:,1] = polidata
np.savetxt("p04.out", textdata)


print(polirange)
plt.show()
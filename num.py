

#Created by Jagtar Singh
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["January", "February", "March", "April"])
y = np.array([45000, 52000, 65000, 88000])

plt.xlabel("Months(2021)")
plt.ylabel("COVID-19 Cases")

plt.bar(x,y)
plt.show()

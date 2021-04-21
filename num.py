# #Three lines to make our compiler able to draw:
# import sys
# import matplotlib


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 500])

# plt.xlabel("Weeks")
# plt.ylabel("Covid Case")

# plt.plot(xpoints, ypoints)
# plt.show()



# #Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["January", "February", "March", "April"])
y = np.array([45000, 52000, 65000, 88000])

plt.xlabel("Months(2021)")
plt.ylabel("COVID-19 Cases")

plt.bar(x,y)
plt.show()
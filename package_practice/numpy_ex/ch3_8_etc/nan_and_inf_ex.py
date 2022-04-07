#####https://wikidocs.net/32977

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [4,5,6,7]
y2 = [2,3,1,np.nan]
plt.plot(x,y1)
plt.plot(x,y2)

# infinite

maximum = -np.inf
minimum = np.inf

for d in y1:
    if d > maximum:
        maximum = d
    if d < minimum:
        minimum = d

print(maximum, minimum)
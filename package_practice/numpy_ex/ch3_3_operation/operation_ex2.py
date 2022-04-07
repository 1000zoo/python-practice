#####https://wikidocs.net/14597

import numpy as np

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

a = (y**2 + z**2) + 3
print(a)
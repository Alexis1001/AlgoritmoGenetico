import scipy as sp
import matplotlib.pylab as plt
from pylab import *

import matplotlib.pyplot as pl

maximos=[9.35, 9.475, 9.468, 9.549]
minimos=[9.173, 9.186, 9.21, 9.171]
promedios=[9.2397, 9.2757, 9.305, 9.264]

plt.plot(maximos, linestyle='-', label = "peores")
plt.plot(minimos,linestyle=':', label = "mejores")
plt.plot(promedios,linestyle=':', label = "promedio")
plt.legend()
plt.show()
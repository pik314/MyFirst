#!/usr/bin/python

import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

x=range(100)
y=np.array(np.multiply(x,np.pi))
y = np.sin(np.multiply(x,np.pi/20.0))

plt.plot(x,y)
plt.show()


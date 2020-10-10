# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:19:17 2020

@author: Keyvan
"""

import math
import pylab
import numpy as np

x , y = [], []
for i in np.arange(-2 * (np.pi), 2 * np.pi, .1 ):
    print(i)
    x.append(i)
    y.append((math.sin(i)) ** 2)

pylab.plot(x, y)
pylab.show()
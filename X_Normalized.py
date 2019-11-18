# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:15:19 2019

@author: JUSTIN
"""

import numpy as np
r = np.random.random((5,5))
m = np.mean(r)
sd = np.std(r)

Z = (r-m)/sd

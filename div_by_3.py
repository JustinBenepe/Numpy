# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 07:23:47 2019

@author: JUSTIN
"""

A = np.arange(1,101).reshape(10,10)
print ("\n\nThe Matrix is \n\n"+str(A*A))

B = (A*A)%3
a,b = np.where(B == 0)

C = A*A
D = C[a,b]
print ("\n\nThe Number which are divisible by 3 are \n\n"+str(D))
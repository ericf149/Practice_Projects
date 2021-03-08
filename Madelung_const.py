# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:50:08 2021

@author: Eric
"""

from math import sqrt

def oddOrEven(i,j,k):
    total = i + k + j
    if total % 2 == 0: return 0
    if total % 2 != 0: return 1

L=200
V=0
for i in range(-L,L):
    for j in range(-L,L):
        for k in range(-L,L):
            if i==0 and j==0 and k==0: continue
            Vturn = 1 / sqrt(i**2+j**2+k**2)
            if oddOrEven(i, j, k) == 1:
                V = V - Vturn
            if oddOrEven(i, j, k) == 0:
                V = V + Vturn

print("Madelung constant: ", V)
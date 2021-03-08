# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:13:04 2021

@author: Eric
"""

from math import factorial as fac

def binomial(n,k):
    if k==0: return 1
    Bino = fac(n) // fac(k) // fac(n-k)
    return int(Bino)


prob = binomial(100,60) / 2**100

def coinProb(n,k):
    sums = []
    for i in range(k,n):
        sums.append(binomial(n,i)*.5**k*.5**(n-k))
    return sum(sums)

print(coinProb(100, 60))

print(prob)
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:52:31 2021

@author: Eric
"""

from math import factorial as fac

def binomial(n,k):
    if k==0: return 1
    Bino = fac(n) // fac(k) // fac(n-k)
    return int(Bino)


def pascal(m):
    for x in range(m+1):
        print([binomial(x,y) for y in range(x+1)])
    

n = int(input("n:"))
k = int(input("k:"))
m = int(input("m:"))
print("Coefficient:", binomial(n, k))
pascal(m)
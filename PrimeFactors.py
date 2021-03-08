# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:54:19 2021

@author: Eric
"""

import math

def primeFactors(k):
    primelist= [2,3]
    for n in range(2,k+1):
        sqrtn = math.sqrt(n)
        for j in primelist:
            if n%j!=0 and j<=sqrtn:
                print(n,j)
                primelist.append(n)
                break
            print(primelist)
    return primelist


#print(primeFactors(20))


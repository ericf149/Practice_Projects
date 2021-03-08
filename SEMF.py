# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:37:14 2021

@author: Eric
"""

#A = int(input("Mass number:"))
#Z = int(input("Atomic number:"))


#coefficients, all in eV
a1 = 15.8 
a2 = 18.3
a3 = 0.714
a4 = 23.2

def a5value(A,Z):
    if A%2==1: return 0
    if A%2==0 and Z%2 ==0: return 12.0
    if A%2==0 and Z%2 ==1: return -12.0
    


def stableA(Z):
    Amax=0
    Avalue= []
    for A in range(Z, 3*Z):
        a5 = a5value(A, Z)
        Bind = a1*A - a2*A**(2/3) - a3*Z**2 /A**(1/3) - a4*(A-2*Z)**2 /A + a5 / A**(1/2)
        Avalue.append(Bind/A)
        print("1:",A)
        print("2:", Avalue)
        print("3:", max(Avalue))
        if max(Avalue)==Bind/A: Amax=A
        print("4:", Amax)
        return Amax
    
for Z in range(1,100):
    Am = stableA(Z)
    print("Z:", Z)
    print("Max A:", Am)

#print("Binding Energy:", Bind)
#print("Binding Energy:", Bind/A)
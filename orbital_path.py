# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:48:03 2021

@author: Eric
"""
from math import sqrt, pi

G=float(6.67*10**-11) #m^3 kg^-1 s^-2
M=float(1.9891*10**30) #kg

l1 = float(input("Perihelion Distance:"))
v1 = float(input("Perihelion Velocity:"))

v2 = (G*M/(l1*v1)) - sqrt((G*M/(l1*v1)) + (v1**2*l1-2*G*M)/l1) #aphelion velocity in m/s
l2 = l1*v1 / v2 #perihelion distance in m 

A = .5*(l1+l2)
B = sqrt(l1*l2)
T = (2*pi*A*B)/(l1*v1)
E = (l2-l1)/(l1+l2)

print("Aphelion Distance:", l2)
print("Aphelion Velocity:", v2)
print("Orbital Period:", T)
print("Orbital Eccentricity:", E)

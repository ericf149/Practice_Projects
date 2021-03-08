# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:25:08 2021

@author: Eric
"""
import math

m = 9.11*10**-31 #electron mass in kg
E = 10 # electron energy in eV
V = 9 # step energy in eV
hbar = 1.05*10**-34 #reduced planck const. in Joule seconds

k1 = math.sqrt(2*m*E)/hbar
k2 = math.sqrt(2*m*(E-V))/hbar

Trans = 4*k1*k2 / (k1+k2)**2
Refle = ((k1-k2)/(k1+k2))**2

print("Transmission Probability:", Trans)
print("Reflection Probability:", Refle)


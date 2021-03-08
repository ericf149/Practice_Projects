# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:24:34 2021

@author: Eric
"""
import math

G=float(6.67*10**-11) #m^3 kg^-1 s^-2
M=float(5.97*10**24) #kg
R=6371000 #m

T=float(input("Orbit Time: ")) #seconds!!

h = ( G * M * T**2 / (4 * math.pi**2))**(1/3) - R
print("Orbit Altitude:", h,"meters") #output in meters
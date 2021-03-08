# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:05:32 2021

@author: Eric
"""
import math

c=299792458 #m/s
v=.99*c #m/s but use units of c
d=10 #ly= distance of c*1year
gamma = 1/math.sqrt(1-(v**2/c**2))

t=10/.99
print("Spaceship frame time:", t)

tproper= t*gamma
print("Earth frame time:", tproper)

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 01:33:31 2021

@author: Eric
"""
import math
import numpy as np
from matplotlib import pyplot as plt 


#salary = float(input("Salary:"))

# tax brackets
#10% under 9875
#12% under 40125
#22% under 85525
#24% under 163300
#32% under 207350
#35% under 518400
#37% over 518401

percents = [.10,.12,.22,.24,.32,.35,.37]
brackets = [0,9875,40125,85525,163300,207350,518400]

def SalaryReduced(salary):
    taxtotal=0
    for i in range(1,len(brackets)-1):
        if salary >= brackets[i]:
            #print("i1:",i)
            tax=(brackets[i]-brackets[i-1])*percents[i-1]
            #print("Sal, brack, perc:", salary, brackets[i-1], percents[i-1])
            #print("Tax1:",tax)
            taxtotal+=tax
            #print("Total1:",taxtotal)
        if salary < brackets[i]:
            #print("i2:",i)
            taxover=(salary - brackets[i-1])*percents[i-1]
            #print("Sal, brack, perc:", salary, brackets[i-1], percents[i-1])
            #print("Taxover:", taxover)
            taxtotal+=taxover
            break
    if salary >= brackets[-1]:
        #print("i3:")
        taxplus = (salary - brackets[-1])*percents[-1]
        taxtotal+=taxplus
    #print("Total:", taxtotal)
    return taxtotal

plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 

xlist = []
ylist = []

X = np.arange(1000,1000000,100)
for x in X:
    y = x/SalaryReduced(x)
    xlist.append(x)
    ylist.append(y)
    
plt.xlim(1000, 1000000)
plt.ylim(0,12)
plt.plot(xlist,ylist)


plt.show()


# for y in range(len(brackets)-1):
#     if salary >= brackets[y]: # not necessary tbh, just for more info
#         print("y:",y) #so i can see progress
#         continue
#     if salary < brackets[y]:
#         print("y:",y)
#         BrackSum= sum(taxedInc[:y]) #sum all values in list up to marginal bracket
#         print("BrackSum:", BrackSum)
#         taxleft=(salary-brackets[y-1])*percents[y] #find tax on marginal bracket overflow
#         print("taxleft:", taxleft)
#         taxtotal = BrackSum + taxleft #total amount of tax on all salary
#         break
# print(taxtotal)
# def Salaryloss(salary):
#     taxtotal=0
#     for x in range(len(percents)-1):
#         print("1:",x)      
#         if salary > brackets[-1]:
#             taxover=(salary-brackets[-1])*percents[-1]
#             taxtotal+=taxover
#             print("4:", taxtotal,"||", taxover)
#         if salary>=brackets[x]:
#             tax = brackets[x]*percents[x]
#             taxtotal+=tax
#             print("2:", taxtotal,"||", tax)
#             continue
#         if salary<brackets[x]:
#             lefttax=(salary - brackets[x-1])*percents[x-1]
#             print("X:", brackets[x-1], percents[x])
#             taxtotal+=lefttax
#             print("3:", taxtotal,"||", tax)
#             break
#         print("5:", taxtotal)
#         NewSal = salary-taxtotal
#         return NewSal
            
            

#print("Reduced Salary:", SalaryReduced(salary))
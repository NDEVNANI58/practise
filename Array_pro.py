# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:24:34 2020

@author: hp1
"""

## Sum of Array
import numpy as np
a=np.array([1,2,3,4,5],"i")
#a.sum()
t=0
for i in range(0,len(a)):
    t=t+int(a[i])
    
## largest element in array
a=np.array([2,1,3,5,4],"i")
a.max() 

for i in range(0,len(a)):
    if(i<4):
        if(a[i]>=a[i+1]):
             t=a[i]
             a[i]=a[i+1]
             a[i+1]=t
    d=int(a[len(a)-1])
    print(a[i])

##rotating the array
    n=int(input("till what position u want to rotate"))
a=np.array([2,1,3,5,4],"i") 
b=[]
for i in range (0,len(a)):
    if(i<n):
        b.append(a[i])
        a[i]=a[i+2]
    elif(i==n or i<len(a)-1):
        a[i]=a[i+2]
a[n+1:]=b
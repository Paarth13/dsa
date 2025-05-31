#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    i=0
    j=i+1
    count=0
    k=0
    n=len(arr)
    while(i<n and j<n):
        diff1=arr[j]-arr[i]
        f=1
        if  diff1==d:
            if f==1:
                f=0
                k=j+1
            while (k<n):
                diff2=arr[k]-arr[j]
                if diff2==d:
                    print (i,j,k)
                    count+=1
                    break
                if diff2>d:
                    k-=1
                    break
                k+=1
        if diff1>d:
            i+=1
            j-=1
        else:
            j+=1
    return count
def teste():
    var x
    var y=0
    if x:
        print (y)
if __name__ == '__main__':
    # result = beautifulTriplets(3, [1 ,6 ,7 ,7 ,8 ,10 ,12 ,13 ,14 ,19])
    # print (result)
    teste()n
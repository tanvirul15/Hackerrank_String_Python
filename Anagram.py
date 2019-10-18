#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    l=len(s)
    if l%2==1:
        return -1
    mid=l//2
    li2=[]
    for i in range(0,mid):
        li2.append(s[i])
    count=0
    for i in range(mid,l):
        if s[i] in li2:
            count+=1
            li2.remove(s[i])
    return mid-count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

import sys
import numpy as np
from collections import defaultdict

permdict=defaultdict(int)

def factorial(n):
    if (n==0):
       return 1
    else:
       return n*factorial(n-1)

def genpermutations(digits):
    numperm = factorial(len(digits))
    summation = 0
    numbers = 1
    while len(permdict) != numperm:
        perms = np.random.permutation(digits) 
        permnumber = int("".join(perms.tolist()))
        if permdict[permnumber] > 0:
            continue
        permdict[permnumber] = numbers
        numbers += 1
        summation += permnumber
    print("summation:",summation)
    print("permutations:",permdict)
    print("numbers:",numbers-1)

if __name__=="__main__":
    genpermutations(['0','2','4','6','8'])

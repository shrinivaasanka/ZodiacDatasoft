import numpy as np
from functools import reduce

def array_intersection(arrays):
    cnt=0
    intersection=[]
    intersecting_indices=[]
    for cnt in range(len(arrays[0])):
        arraytuple=()
        for a in arrays:
            arraytuple = arraytuple + (a[cnt],)
        print("arraytuple:",arraytuple)
        intersection.append(reduce(np.intersect1d,arraytuple))
        for n in range(len(arrays)-1):
            intersecting_indices.append(np.intersect1d(arrays[n],arrays[n+1],return_indices=True))
    print("intersection:",intersection)
    print("intersecting indices:",intersecting_indices)

if __name__=="__main__":
    bitmaparray1=[[1,1,1,0,0,0,1,1],
              [0,1,0,0,1,0,1,0],
              [1,1,0,0,1,1,1,0],
              [1,1,1,0,1,1,1,0],
              [1,1,1,0,1,1,1,1],
              [1,1,1,0,1,1,1,0],
              [1,1,1,0,1,1,1,1],
              [1,1,1,0,1,1,1,0]]
    bitmaparray2=[[1,1,1,0,0,0,1,1],
              [0,1,1,1,1,0,1,0],
              [1,1,0,1,1,1,1,0],
              [1,1,1,1,1,0,1,0],
              [1,1,1,0,1,1,1,1],
              [1,1,1,0,0,0,1,0],
              [1,1,1,0,1,1,1,1],
              [1,1,1,0,1,1,1,0]]
    bitmaparray3=[[1,1,1,0,0,0,1,1],
              [0,1,0,1,1,0,1,0],
              [1,1,0,1,1,1,1,0],
              [1,1,0,1,1,0,1,0],
              [1,1,1,0,0,1,1,1],
              [1,1,1,0,0,1,1,0],
              [1,1,1,1,1,1,1,1],
              [1,1,1,0,1,1,1,0]]
    array_intersection([bitmaparray1,bitmaparray2,bitmaparray3]) 
    string1=[['f','i','r','s','t','n','a','m','e']]
    string2=[['l','a','s','t','n','a','m','e']]
    string3=[['s','u','r','n','a','m','e']]
    string4=[['m','i','d','d','l','e','n','a','m','e']]
    array_intersection([string1,string2,string3,string4]) 

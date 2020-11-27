import numpy as np

def gmat(p): 
    # returns chao matrix for given value of p
    mat = [[int(x) for x in i.split(' ')] for i in
        open('chaomat.txt','r').read().strip().split('\n')]
    for i in range(9):
        for j in range(9):
            if mat[i][j]==-1:
                mat[i][j]=2*p-1
    return np.array(mat)

def nev(p):    # verify that all are positive eigen values 
    eigv = np.linalg.eig(gmat(p))[1]
    # extra step: to ensure that the eigen vectors are orthogonal
    for i in range(len(eigv)):
        for j in range(i):
            if eigv[i] @ eigv[j] !=0:
                return False
    return all(np.linalg.eig(gmat(p))[0]>-0.000000001) # to accomodate for python float precision

print("part2.py")

MIN = 0
MAX = 1
while abs(MAX-MIN) > 0.00001:
    MID = (MIN + MAX)/2
    if nev(MID):
        MAX=MID
    else:
        MIN=MID
    # print(MAX,MIN,MID)
print("The threshold value after binary search is :", MAX)

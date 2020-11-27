import numpy as np

print("part1.py")
mat = [[int(x) for x in i.split(' ')] for i in
    open('chaomat.txt','r').read().strip().split('\n')]

print(np.linalg.eig(mat)[0], 'Are the eigen values of the chao matrix in file chaomat.txt')
print('We can see that there is a negative eigen value, proving to us that the map is not completely positive')



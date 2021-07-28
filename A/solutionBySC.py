#------------------------
# There are some errors, but program works
#--------------------------

from math import *

size=int(input('enter size of grid:'))
lst=[]

for _ in range(size):
    for _ in range(size):
        lst.append(int(input()))
print(lst)

pos=0
c=lst[0]
print(c)

if lst[1]<lst[size]:
    c=floor(c/2) + lst[1]
    pos += 1
else:
    c=floor(c/2) + lst[size]
    pos += size

print(c)
print('place in matrix:',pos)

for _ in range(size+(size-3)):
    if int(pos+1) % size == 0:
        c=floor(c/2) + lst[pos+size]
        pos += size
    elif pos>size**2-size:
        c=floor(c/2)+lst[pos+1]
        pos += 1
    elif lst[pos+1]<lst[pos+size]:
        c=floor(c/2) + lst[pos+1]
        pos += 1
    else:
        c=floor(c/2) + lst[pos+size]
        pos += size
    print(c)
    print('place in matrix:',pos)
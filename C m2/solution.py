# Dole Out Cadbury

min_len  = int(input())
max_len = int(input())

min_wid = int(input())
max_wid = int(input())

'''
static input
'''
# min_len  = 5
# max_len = 7

# min_wid = 3
# max_wid = 4

cadbury_in_box = []

for l in range(min_len, max_len + 1):
    for w in range(min_wid, max_wid + 1):
        cadbury_in_box.append([l, w])

'''
makes a given size squre and returns list of squre sizes, recursively
'''
def make_squre(size):
    temp = []
    if(max(size) == 1):
        return [[1, 1]]
    elif(max(size) == min(size)):
        return [size]
    else:
        temp.append([min(size), min(size)])
        temp += make_squre([max(size) - min(size), min(size)])
        return temp

squre_cadbury = []
for size in cadbury_in_box:
    squre_cadbury += make_squre(size)

print(len(squre_cadbury))

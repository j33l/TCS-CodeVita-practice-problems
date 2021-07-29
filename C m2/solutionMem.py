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
makes a given size squre and returns number of squres, recursively
'''
def make_squre(size):
    if max(size) in [1, min(size)]:
        return 1
    temp = 0
    return temp + 1 + make_squre([max(size) - min(size), min(size)])

squre_cadbury = sum(make_squre(size) for size in cadbury_in_box)
print(squre_cadbury)

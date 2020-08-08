#

# quantity_of_petrol = [int(i) for i in input().split(' ')]

'''
static input
'''
quantity_of_petrol = [1, 2, 3, 4, 5, 10, 11, 3, 6, 16]
# quantity_of_petrol = [25, 30, 35, 20, 90, 110, 45, 70, 80, 12, 30, 35, 85]


quantity_of_petrol.sort()

pump_1 = []
pump_2 = []

# for vehicle in quantity_of_petrol:
#     if(sum(pump_1) > sum(pump_2)):
#         pump_2.append(vehicle)
#     else:
#         pump_1.append(vehicle)
        
# diff = sum(pump_1) - sum(pump_2)
# while diff < max(pump_1) and diff > min(pump_2):
#     pump_1[pump_1.index(max(pump_1))], pump_2[pump_2.index(min())]

m = len(quantity_of_petrol) // 2

pump_1, pump_2 = quantity_of_petrol[: m], quantity_of_petrol[m :]

def find_diff(l1, l2):
    return abs(sum(l1) - sum(l2))

diff = find_diff(pump_1, pump_2)

p = 0
while diff > find_diff(quantity_of_petrol[: p], quantity_of_petrol[p :]):
    pump_1.append(pump_2[p])
    del pump_2[p]
    diff = find_diff(pump_1, pump_2)
    p += 1


print(pump_1, sum(pump_1))
print(pump_2, sum(pump_2))

# print(max(sum(pump_1), sum(pump_2)))

# for i in range(1.00, 3.00, 0.01):
#     print(i)


# x = 1.00
# y = 3.00
# while x != y:
#     print(x)
#     x += 0.01


# import decimal

# def float_range(start, stop, step):
#   while start < stop:
#     yield float(start)
#     start += decimal.Decimal(step)

# print(list(float_range(1.00, 2.00, '0.01')))


# from numpy import arange

# print("Float range using NumPy arange():")

# print("\nTest 1:")
# for i in arange(1.00, 3.00, 0.01):
#     print(i, end=', ')


import numpy as np
 
print("Print Float Range Using NumPy LinSpace()\n")

print(np.linspace(1.00, 3.00))
# print(np.linspace(0, 10, num = 5, endpoint = False))

'''
Solution for "Philaland Coin" problem
by Smit J.
'''


t = int(input()) # `t` is no. of testcases
if not 1 <= t <= 100:
    exit()

all_max_prices = []
for _ in range(t):
    n = int(input()) # `n` is price of costliest item on island
    if not 1 <= n <= 5000:
        exit()
    all_max_prices.append(n)

main_sequence=[]
for each_max in all_max_prices:
    coin_sequence = [k for k in range(1, int(each_max) + 1)]
    main_sequence.append(coin_sequence)
# print(main_sequence)

'''
main logic to reduce number of coins
-> So when the sum of first minimum coin values if more of equal to max coin value, we will stop adding more coins in list
'''
reduced_main_sequence=[]
for seq in main_sequence:
    coinSum = 0
    count = 0
    for priceVal in seq:
       coinSum += priceVal
       count += 1
       if coinSum >= seq[-1]:
           break
    print(f'min no. of coins is {count}, and sum is {coinSum}.')
    print(count, end='\n')

# swayamvar

N = int(input()) # number of groom or bride
brides_to_be = list(input())
grooms_to_be = list(input())

number_of_pairs_left_unmatched = N

for bride in brides_to_be:
    if bride in grooms_to_be:
        # brides_to_be.remove(bride)
        grooms_to_be.remove(bride)
        number_of_pairs_left_unmatched -= 1
    else:
        break

print(number_of_pairs_left_unmatched)

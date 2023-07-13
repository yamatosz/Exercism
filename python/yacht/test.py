import yacht

print(yacht.score([1, 2, 2, 3, 5], yacht.TWOS))
print(yacht.score([1, 1, 1, 1, 1], yacht.YACHT))
print(yacht.score([5, 5, 5, 5, 5], yacht.YACHT))
print(yacht.score([1, 1, 1, 1, 2], yacht.YACHT))
print(yacht.score([4, 2, 4, 4, 2], yacht.FULL_HOUSE))
print(yacht.score([1, 6, 6, 6, 6], yacht.FOUR_OF_A_KIND))
print(yacht.score([1, 5, 5, 5, 5], yacht.FOUR_OF_A_KIND))
print(yacht.score([3, 5, 4, 1, 2], yacht.LITTLE_STRAIGHT))
print(yacht.score([3, 5, 4, 6, 2], yacht.BIG_STRAIGHT))

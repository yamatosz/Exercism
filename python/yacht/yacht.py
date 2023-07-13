# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list, category):
    if category in range(1, 7):
        return dice.count(category) * category
    if category == 0:
        return 50 if dice[0]*5 == sum(dice) else 0
    if category == 7:
        numbers = list(set(dice))
        if len(numbers) != 2:
            return 0
        sum_dice = sum(dice)
        return sum_dice if sum_dice == numbers[0]*3 + numbers[1]*2 or sum_dice == numbers[1]*3 + numbers[0]*2 else 0
    if category == 8:
        numbers = list(set(dice))
        for number in numbers:
            if dice.count(number) >= 4:
                return number*4
        return 0
    if category == 9:
        return 30 if list(set(dice)) == [1, 2, 3, 4, 5] else 0
    if category == 10:
        return 30 if list(set(dice)) == [2, 3, 4, 5, 6] else 0
    if category == 11:
        return sum(dice)

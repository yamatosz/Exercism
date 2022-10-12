"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds = []
    for index_n  in range(0,3):
        rounds.append(number+index_n )
    return rounds

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1+rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds

def card_average(hand:list):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)

def approx_average_is_average(hand: list):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return:   bool - does one of the approximate averages equal the `true average`?
    """
    median = (hand[0]+hand[-1])/2
    middle = hand[round(len(hand)/2)]
    return median == card_average(hand) or middle == card_average(hand)

def average_even_is_average_odd(hand: list):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    average_even = []
    average_odd = []
    index_n = 0
    for index in hand:
        if index_n % 2 == 0:
            average_even.append(index)
        else:
            average_odd.append(index)
        index_n+=1
    return card_average(average_even) == card_average(average_odd)

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[2] == 11:
        hand[2] = 22
    return hand

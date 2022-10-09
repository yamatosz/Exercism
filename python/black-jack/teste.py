from black_jack import (value_of_card, 
                        higher_card, 
                        value_of_ace, 
                        is_blackjack, 
                        can_split_pairs,
                        can_double_down)

print(value_of_card('4'))
print(value_of_card('A'))
print(value_of_card('K'))
print(higher_card('10', 'K'))
print(higher_card('4', '6'))
print(value_of_ace('6', 'K'))
print(value_of_ace('7', '3'))
print(value_of_ace('2', 'A'))
print(value_of_ace('A', '2'))
## print(is_blackjack('A','K'))
## print(is_blackjack('10', '9'))
## print(can_split_pairs('Q', 'K'))
## print(can_split_pairs('10', 'A'))
## print(can_split_pairs('10', 'A'))
## print(can_double_down('A', '9'))
## print(can_double_down('10', '2'))

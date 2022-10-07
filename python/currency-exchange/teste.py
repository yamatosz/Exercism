from exchange import (exchange_money, 
                      get_change,
                      get_value_of_bills,
                      get_number_of_bills,
                      get_leftover_of_bills,
                      exchangeable_value)

print(exchange_money(127.5, 1.2))
print(get_change(127.5, 120))
print(get_value_of_bills(5, 128))
print(get_number_of_bills(127.5, 5))
print(get_leftover_of_bills(127.5, 20))
print(exchangeable_value(127.25, 1.20, 10, 5))
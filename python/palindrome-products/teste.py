from palindrome_products import largest, smallest

def return_list(n, m):
    _list = []
    for num in range (n, m + 1):
        _list.append(num)
    return _list 

def list_products(n, m):
    ##products = return_list(n, m)
    alist = []
    for num in range(n, m+1):
        for num2 in range(n, m+1):
            alist.append(num * num2)
    return remove_duplicates(alist)
    
def remove_duplicates(lista: list):
    _list2 = []
    for num in lista:
        if not num in _list2:
            _list2.append(num)
    _list2.sort()
    return _list2

def is_palindrome(n: int):
    n = str(n)
    return n == n[::-1]

def list_small_palindrome(list):
    ##small = 0
    for n in list :
        if is_palindrome(n):
            return n
    return 'not has a palindrome'

def list_larger_palindrome(list):
    for n in list[::-1]:
        if is_palindrome(n):
            return n
    return 'not has a palindrome'
##print(list_small_palindrome([10, 11, 12, 121]))
##print(list_larger_palindrome([10, 11, 12, 121]))
##print(list_larger_palindrome([14, 15, 18, 16]))
##print(list_small_palindrome(list_products(10, 99)))
##print(list_larger_palindrome(list_products(10, 99)))

def factors(n, min, max):
    factors_ = []
    for x in range(min, max):
        for y in range(min, max+1):
            if x*y == n:
                factors_.append((x, y))
    return factors_

##print(factors(9, 1, 9))
##print(list_small_palindrome(10, 99))
import math

list2 = []
lst = []


def prime(*liczby):
    for i in liczby:
        if i == 2:
            print(i, "is a prime")
        if i % 2 == 0 or i <= 1:
            print(i, "is not a prime")
    return list2




def is_prime(*numb):
    for n in numb:
        if n < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, "is a prime")

is_prime(1, 2, 5, 7)
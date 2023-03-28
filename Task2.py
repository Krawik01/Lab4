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
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i) != 0:
                print(n, "is a prime")


is_prime(1, 3, 5, 6)
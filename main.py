def prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")

prime(5)
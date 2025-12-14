import math
def prime(a, b):
    primes = []
    for i in range(a, b):
        if i < 2:
            continue
        for num in range(2, int(math.sqrt(i)+1)):
            if i % num == 0:
                break
        else:
            primes.append(i)
    print(primes)


prime(1, 100)

#largest prime factor of 600851475143

import math

wan_primeF = []

def prime_factors(num):
    while num % 2 == 0:
        print(2, )
        num = num / 2
        wan_primeF.append(2)

    #i don't undrerstand loop below so I copied from https://www.javatpoint.com/python-program-to-print-prime-factor-of-given-number#:~:text=The%20prime_factor()%20function%20is,square%20root%20of%20n%20times.
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i, )
            num = num / i
            wan_primeF.append(i)
    if num > 2:
        print(num)
    return num

num = 600851475143
prime_factors(num)

#so we have
print(wan_primeF)
print('largest prime factor of that number is: ', max(wan_primeF))
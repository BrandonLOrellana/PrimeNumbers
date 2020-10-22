#!/usr/bin/python
from math import sqrt, floor

def is_prime(num, factors):
    if sqrt(num)>factors[-1]:
        raise ValueError("Number too big to test")
    elif num == 1:
        return False
    for i in factors:
        if i > floor(sqrt(num)):
            break
        if num%i==0:
            return False
    return True


def file_len(filename):
    try:
        return sum(1 for line in open(filename))
    except:
        return 0


def load_primes(filename='primes.txt'):
    if file_len(filename) == 0:
        with open(filename, 'w') as f:
            print(2, file=f)
    return [int(line) for line in open(filename, 'r').readlines()]

def update_primes(nums, filename='primes.txt'):
    with open(filename, 'w') as f:
        f.seek(0)
        for i in nums:
            f.write(str(i) + '\n')
            
            
            
            
primes = load_primes()

for i in range(3, 1000, 2):
    if is_prime(i, primes):
        primes.append(i)

update_primes(primes)




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
    l = file_len(filename)
    nums = nums[l:]
    print(l, nums)
    with open(filename, 'a') as f:
        for i in nums:
            f.write(str(i) + '\n')
            
            
def main():
    primes = load_primes()

    for i in range(primes[-1]+1, primes[-1] + 1001):
        if is_prime(i, primes):
            primes.append(i)
            
    update_primes(primes)

if __name__ == '__main__':
    main()

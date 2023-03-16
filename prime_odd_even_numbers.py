nums = range(50)

prime_doc = """
There are many algorithms for calculating prime numbers, but one of the most common and efficient ones is called the Sieve of Eratosthenes. Here are the steps:

Create a list of all integers from 2 to the highest number you want to check for primality.

Start with the first number in the list (which is 2), and cross out all of its multiples (i.e., every second number in the list).

Move to the next unmarked number in the list (which is 3), and cross out all of its multiples (i.e., every third number in the list).

Repeat step 3 with the next unmarked number until you have crossed out all of the multiples of all the primes up to the square root of the highest number.

The remaining unmarked numbers in the list are all primes.

For example, to calculate all the prime numbers between 2 and 30, you would start with the list:

2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

Then you would cross out all the multiples of 2 (i.e., 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, and 30), leaving:

2 3 5 7 9 11 13 15 17 19 21 23 25 27 29

Then you would cross out all the multiples of 3 (i.e., 9, 15, 21, and 27), leaving:

2 3 5 7 11 13 17 19 23 25 29

At this point, you have crossed out all the multiples of all the primes up to the square root of 30, which is 5. So you can stop here and conclude that the remaining unmarked numbers are all primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29.
"""


def is_prime(num):
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                return False
        return True


prime = list(filter(is_prime, nums))
print(prime)


# for i in prime:
#     print(i)
odd_doc ="""Odd numbers are numbers that cannot be divided by 2 without leaving a remainder. To calculate odd numbers, you can use the following formula:

Odd number = 2n + 1

where n is a non-negative integer. By plugging in different values of n, you can generate a sequence of odd numbers. For example:

n = 0: 2n + 1 = 2(0) + 1 = 1
n = 1: 2n + 1 = 2(1) + 1 = 3
n = 2: 2n + 1 = 2(2) + 1 = 5
n = 3: 2n + 1 = 2(3) + 1 = 7
n = 4: 2n + 1 = 2(4) + 1 = 9
n = 5: 2n + 1 = 2(5) + 1 = 11

And so on. This formula generates an infinite sequence of odd numbers, and you can calculate as many odd numbers as you need by plugging in different values of n.



"""
def is_odd(num):
    if num + 1:
        for i in range(num):
            if (num % 2) != 0:
                return True
        return False


odd = list(filter(is_odd, nums))
print(odd)

even_doc = """Even numbers are numbers that are divisible by 2 without leaving a remainder. To calculate even numbers, you can use the following formula:

Even number = 2n

where n is a non-negative integer. By plugging in different values of n, you can generate a sequence of even numbers. For example:

n = 0: 2n = 2(0) = 0
n = 1: 2n = 2(1) = 2
n = 2: 2n = 2(2) = 4
n = 3: 2n = 2(3) = 6
n = 4: 2n = 2(4) = 8
n = 5: 2n = 2(5) = 10

And so on. This formula generates an infinite sequence of even numbers, and you can calculate as many even numbers as you need by plugging in different values of n. Note that 0 is also an even number, since it is divisible by 2 without leaving a remainder.




"""
def is_even(x):
    for i in range(x):
        if (x % 2) == 0:
            return True
        return False

#list comprehension
even = list(filter(is_even, nums))
print(even)
my_even = [x for x in range(100) if x >= 2 and x % 2 == 0]
print(my_even)
my_odd = [x for x in range(100) if x >= 1 and x % 2 != 0]
print(my_odd)
y = range(100)
my_prime = [x for x in range(100) if x >= 1 and x % 2 != 0 and x % 3 != 0]

print(my_prime)

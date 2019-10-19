# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Problem 5 - Smallest Multiple


def smallest_multiple():
    n = 1
    divider = 1

    while n % divider == 0:

        if divider == 20:
            print("Smallest Number Divisible with all numbers 1-20 is " + str(n))
            break

        else:
            divider += 1

        if n % divider != 0:
            n += 1
            divider = 1
            print("[*] Searching " + str(n))


print(smallest_multiple())

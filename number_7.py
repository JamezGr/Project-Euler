# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Problem 7 - 10001st prime

position = 10001


def get_factors(number):

    n = 1
    all_factors = []

    while n < number + 1:
        if number % n == 0:
            all_factors.append(n)

        n += 1

    if len(all_factors) == 2:

        return "True"

    else:

        return "False"


def get_prime(number):
    prime_list = []
    n = 1

    while len(prime_list) < number:
        if get_factors(n) == "True":
            prime_list.append(n)
            print("Appended " + str(prime_list[-1]))

        n += 1

        if len(prime_list) == number:
            break

    return prime_list[number - 1]


print(str(get_prime(position)) + " is Prime Number " + str(position))

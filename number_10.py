# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

limit = 1000


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

        n += 1

        if len(prime_list) > 1:
            last_number = prime_list[-1]

            if last_number > number:
                del prime_list[-1]
                break

    return prime_list


def split_string():
    n = 0
    split_sum = ""

    while n < len(get_prime(limit)):
        split_sum += str(get_prime(limit)[n]) + " + "

        n += 1

        if n == len(get_prime(limit)) - 1:
            split_sum += str(get_prime(limit)[-1])
            break

    return split_sum


print(get_prime(limit))
print("The Sum Of All the Prime Numbers Below " + str(limit) + " is: " + str(eval(split_string())))

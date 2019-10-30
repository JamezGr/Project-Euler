# Problem 12 - Highly Divisible Triangular Number
# What is the value of the first triangle number to have over five hundred divisors?


def get_triangle_number(number):
    next_number = 1
    triangle_number = 0

    while next_number <= number:
        triangle_number += next_number
        next_number += 1

    return triangle_number


def get_factors(triangle_number):
    factor = 1
    list_of_factors = []

    while factor <= triangle_number:
        if triangle_number % factor == 0:
            list_of_factors.append(factor)
        factor += 1

        if factor > triangle_number:
            break

    number_of_divisors = len(list_of_factors)

    return number_of_divisors


def _main_():
    number = 1

    while get_factors(get_triangle_number(number)) < 501:
        print(get_triangle_number(number))

        number += 1

    return get_triangle_number(number)


# print(get_triangle_number(384))
print(_main_())

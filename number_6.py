# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Problem 6 - Sum Square Difference


def sum_square():
    number = 1
    sum_of_square = 0

    while number < 101:
        sum_of_square += number * number
        number += 1

    return sum_of_square


def squared_sum():
    number = 1
    square_of_sum = 0

    while number < 101:
        square_of_sum += number
        number += 1

    return square_of_sum * square_of_sum


print("The Square of The Sum is " + str(squared_sum()))
print("The Sum of The Square is " + str(sum_square()))
print("\nThe Difference is " + str(squared_sum() - sum_square()))


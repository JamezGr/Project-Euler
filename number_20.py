# Factorial digit sum
# Problem 20
# Find the sum of the digits in the number 100!

factorial_number = 1

for number in xrange(100, 0, -1):
    factorial_number *= number

numbers_to_add = [int(x) for x in str(factorial_number)]

print(sum(numbers_to_add))

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def check_palindrome(num):

    return str(num) == str(num)[::-1]


def fn(n):
    max_palindrome = 1
    for x in range(n, 1, -1):
        for y in range(n, x-1, -1):
            if check_palindrome(x*y) and x*y > max_palindrome:
                max_palindrome = x*y
            elif x * y < max_palindrome:
                break
    return max_palindrome


print(fn(999))

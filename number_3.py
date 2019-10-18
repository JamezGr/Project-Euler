def largest_prime_factor(num):
    i = 2

    while True:
        if i * i > num:
            return num

        else:
            if num % i == 0:
                num = num / i
            else:
                i = i + 1


print(largest_prime_factor(600851475143))






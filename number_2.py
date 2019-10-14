fibonacci_sequence = [1, 1]
even_fibonacci = []


while len(fibonacci_sequence) < 33:

    next_term = fibonacci_sequence[-2] + fibonacci_sequence[-1]
    fibonacci_sequence.append(next_term)


for i in fibonacci_sequence:
    if i % 2 == 0:
        even_fibonacci.append(i)


print("\n\n\nSum of Even Numbers: " + str(sum(even_fibonacci)))

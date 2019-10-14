i = 0

common_multiples = []

multiples_of_three = []
multiples_of_five = []

while i < 1000:

    if i % 5 == 0:
        multiples_of_five.append(i)

    if i % 3 == 0:
        multiples_of_three.append(i)

    i += 1

for i in multiples_of_three:
    common_multiples.append(i)

for i in multiples_of_five:
    if i not in multiples_of_three:
        common_multiples.append(i)


print("Sum of All Numbers:  " + str(sum(common_multiples)))


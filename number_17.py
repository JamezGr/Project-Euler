# Problem 17 - Number letter counts

from num_string import num2words

sum_of_letters = []


def produce_words():
    number = 1

    while number < 1001:
        number_string = str(num2words(number)).replace(" ", "")
        character_length = str(len(number_string))
        sum_of_letters.append(character_length)
        number += 1

    return sum_of_letters


produce_words()
total_letters = ' + '.join(sum_of_letters)

print(str(eval(total_letters)) + " Characters Used")



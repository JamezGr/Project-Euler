# Problem 14 - Longest Collatz sequence

collatz_sequence = []


def get_new_number(number):

    if number % 2 == 0:
        number = number / 2

    if number % 2 != 0:
        number = (3 * number) + 1

    return int(number)


# def create_sequence():


def create_sequence(number):

    collatz_sequence.append(number)

    while collatz_sequence[-1] > 2:

        next_number = get_new_number(collatz_sequence[-1])

        if next_number != 1:
            collatz_sequence.append(next_number)

        elif next_number == 2:
            break


def try_new_number():
    number = 14
    list_of_lengths = []

    while number < 1000000:
        create_sequence(number)
        length = len(collatz_sequence) + 1
        list_of_lengths.append(length)
        print("[*] " + str(number))
        number += 1

    max_value = max(list_of_lengths)
    max_index = list_of_lengths.index(max_value)

    print("Number " + str(max_index))


try_new_number()

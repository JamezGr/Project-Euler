# Problem 16 - Power Digit Sum

total = 2 ** 1000

total_string = list(str(total))
total_string = ' + '.join(total_string)

print(eval(total_string))

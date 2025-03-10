def number_length(number):
    if number == 0:
        return 0
    return 1 + number_length((number - number % 10) / 10)

def armstrong_number(number, number_length):
    if number == 0:
        return 0
    tens = number % 10
    return int(tens**number_length + armstrong_number((number - tens) / 10, number_length))

def is_armstrong_number(number):
    return number == armstrong_number(number, number_length(number))

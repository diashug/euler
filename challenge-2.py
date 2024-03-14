import sys

if len(sys.argv) < 2:
    print('Missing limit argument')
    exit(1)

def generate_fibonacci_sequence(limit):
    sequence = [1, 2] # starting from 1 and 2
    for i in range(limit):
        number = sequence[(i + 2) - 1] + sequence[(i + 2) - 2]
        if number <= 4000000:
            sequence.append(number)
            print(sequence[i])
        else:
            break
    return sequence

def is_even(number):
    return number % 2 == 0

def sum_even_fibonacci_numbers():
    sum = 0
    sequence = generate_fibonacci_sequence(int(sys.argv[1]))
    for x in sequence:
        if is_even(x):
            sum = sum + x
    print('sum = ' + str(sum))

sum_even_fibonacci_numbers()
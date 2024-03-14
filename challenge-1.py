import sys

sum = 0

if len(sys.argv) < 2:
    print('Missing limit argument')
    exit(1)

for i in range(int(sys.argv[1])):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i
        print(i)

print(sum)
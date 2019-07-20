# White Magic
numbers = list(int(x) for x in input('Input some numbers: ').split(' '))

total = 0

for i in numbers:
	total += i ** 5

print(total)
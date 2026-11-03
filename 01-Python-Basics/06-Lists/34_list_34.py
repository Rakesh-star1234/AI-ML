
# Q34: Find negative numbers from a list

numbers = [-10, 15, -20, 25, 0, 30, -5]

negative_numbers = []

for number in numbers:
    if number < 0:
        negative_numbers.append(number)

print(negative_numbers)

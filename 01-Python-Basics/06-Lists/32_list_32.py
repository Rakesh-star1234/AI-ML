
# Q32: Find odd numbers from a list

numbers = [10, 15, 20, 25, 30, 35, 40]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)

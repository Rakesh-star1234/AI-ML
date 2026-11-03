
# Q31: Find even numbers from a list

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

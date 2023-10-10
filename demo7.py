def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total

# Taking user input
num = int(input("Enter a positive integer: "))

# Checking if the input is valid
if num < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is {result}")

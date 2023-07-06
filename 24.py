# Implement a function to check if a given number is a power of two.

def is_power_of_two(number):
    if number <= 0:
        return False
    return (number & (number - 1)) == 0

number = int(input("Enter any number: "))
if is_power_of_two(number):
    print(number, "is a power of two.")
else:
    print(number, "is not a power of two.")

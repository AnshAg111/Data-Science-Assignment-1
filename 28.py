#  Implement a function to calculate the square root of a given number.
import math
def square_root(number):
    return math.sqrt(number)

input_number = int(input("Enter any number: "))
print("Square root of", input_number, "is:", square_root(input_number))
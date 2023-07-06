#  Implement a function to find the mode of a list of numbers.

def mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_frequency]
    
    return mode

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Mode:", mode(numbers))

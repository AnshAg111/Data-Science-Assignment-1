# Write a program to find the prime factors of a given number.

def prime_factors(num):
    factors = []
    div = 2
    
    while div <= num:
        if num % div == 0:
            factors.append(div)
            num //= div
        else:
            div += 1
    
    return factors

number = int(input("Enter any number: "))
print("Prime factors of", number, "are:", prime_factors(number))

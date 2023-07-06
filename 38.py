#  Implement a function to find the missing number in a given list of consecutive numbers.

def find_missing_number(l):
    sorted_list=sorted(l)
    for i in range(1, len(l)):
        if sorted_list[i]-sorted_list[i-1]>1:
            return sorted_list[i]-1
    return None

my_list=[1,3,4,5,6,7,8]
print("The missing no. in the list is:", find_missing_number(my_list))
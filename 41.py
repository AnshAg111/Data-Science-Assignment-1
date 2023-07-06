# Write a Python program to find the smallest missing positive integer in a list.

def smallest_missing_number(l):
    sorted_list=sorted(l)
    for i in range(1, len(l)):
        if sorted_list[i]-sorted_list[i-1]>1:
            return sorted_list[i]-1
    return None

my_list=[1,3,4,5,6,7,8,10]
print("The missing no. in the list is:", smallest_missing_number(my_list))
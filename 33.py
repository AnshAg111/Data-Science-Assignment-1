# Write a Python program to remove duplicates from a list while preserving the order.

def remove_duplicates(l):
    unique_list = []
    seen_is = set()

    for i in l:
        if i not in seen_is:
            unique_list.append(i)
            seen_is.add(i)

    return unique_list

my_list = [3, 5, 2, 2, 1, 6, 5, 4, 3, 6]
print("List after removing duplicates:", remove_duplicates(my_list))

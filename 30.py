#  Implement a function to find the minimum element in a rotated sorted list.

def find_minimum(rotated_list):
    left = 0
    right = len(rotated_list) - 1
    if rotated_list[left] <= rotated_list[right]:
        return rotated_list[left]

    while left < right:
        mid = (left + right) // 2

        if rotated_list[mid] > rotated_list[right]:
            left = mid + 1
        else:
            right = mid

    return rotated_list[left]

input_list = [4, 5, 6, 7, 0, 1, 2]
result = find_minimum(input_list)
print("Minimum element:", result)

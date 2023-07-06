# Implement a function to find the maximum subarray sum in a given list.

# using kadane's algorithm
def max_subarray_sum(arr):
    sum=0
    res=float('-inf')
    for i in arr:
        sum+=i
        res=max(sum, res)
        sum=max(sum, 0)
    return res 

nums=[-2,1,-4,4,-1,-3,-1,2,2,1,-5,5,4]
print("The maximum subarray sum=", max_subarray_sum(nums))
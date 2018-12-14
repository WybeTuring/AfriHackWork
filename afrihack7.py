def binary_array_to_number(arr):
    sum = 0;
    for i in range(0,len(arr)):
        sum = sum + arr[i]*(2**(len(arr)-i-1))
    return sum;
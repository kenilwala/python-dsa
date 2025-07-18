def max_sum_subarray(arr,k):
    window_sum = max_sum = sum(arr[:k])

    for i in range(k,len(arr)):
        window_sum = window_sum - arr[i]+arr[i-k]
        max_sum=max(max_sum, window_sum)
    return max_sum

print(max_sum_subarray([2,1,5,1,3,2],3))
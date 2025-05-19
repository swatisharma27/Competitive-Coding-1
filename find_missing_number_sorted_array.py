def missingSortedArray(nums):
    '''
    Time Complexity: O(logn)
    Space Complexity: O(1)
    '''    
    N = len(nums)
    low = 0
    high = N - 1

    while low <= high:
        mid = low + (high-low)//2
        if nums[mid] != mid+1:
            high = mid - 1
        else:
            low = mid + 1

    return low + 1


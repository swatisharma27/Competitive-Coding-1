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
            high = mid - 1 ## Right half eliminated, left half would be traversed to find the missing element
        else:
            low = mid + 1 ## Left half eliminated, right half would be traversed to find the missing element

    return low + 1 # Return the element which would be index+1

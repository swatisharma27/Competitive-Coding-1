def find_missing_in_sorted_array(arr):
    '''
    Time Complexity: O(logn)
    Space Complexity: O(1)
    '''    
    N = len(arr)
    low = 0
    high = N - 1

    while (high - low) >= 2:
        mid = low + (high-low)//2
        lowIndex = arr[low] - low
        midIndex = arr[mid] - mid
        
        if midIndex != lowIndex:
            high = mid 
        else: #midIndex == lowIndex
            low = mid
    
    return (arr[low]+ arr[high])/2

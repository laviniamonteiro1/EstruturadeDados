def twoSum_quickSort_twoPointer(nums, target):
    indexed_nums = [(num, i) for i, num in enumerate(nums)]

    def _quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort_recursive(arr, low, pi - 1)
            _quick_sort_recursive(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high][0] 
        i = low - 1

        for j in range(low, high):
            if arr[j][0] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort_recursive(indexed_nums, 0, len(indexed_nums) - 1)

    left = 0
    right = len(indexed_nums) - 1

    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]

        if current_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
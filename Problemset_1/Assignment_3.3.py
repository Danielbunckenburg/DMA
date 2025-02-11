def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def find_triplet(a):
    n = len(a)
    merge_sort(a)  # Using Merge Sort instead of built-in sort
    
    for i in range(n - 2):
        if i > 0 and a[i] == a[i - 1]:  # Skip duplicates
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = a[i] + a[left] + a[right]
            
            if current_sum == 0:
                return (i, left, right)  # Return indices of the triplet
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return "failed"  # No triplet found

# Example usage:
a = [-1, 2, 1, 0, -2, 3]
result = find_triplet(a)
print(result)

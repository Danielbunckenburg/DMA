def check(A, lo, hi):
    if lo >= hi:
        return True  # Base case: A single element or empty subarray is trivially sorted

    mid = (lo + hi) // 2  # Compute the middle index
    success = True

    # Check if all elements in the left half are <= A[mid]
    for i in range(lo, mid):
        if A[i] > A[mid]:
            success = False
            break

    # Check if all elements in the right half are >= A[mid]
    for i in range(mid + 1, hi + 1):
        if A[i] < A[mid]:
            success = False
            break

    # Recursively check the left and right halves
    if lo < mid and success:
        success = check(A, lo, mid - 1)
    if mid + 1 < hi and success:
        success = check(A, mid + 1, hi)

    return success

# Example usage
A = [1, 2, 2, 3, 4, 5, 6, 7]  # A valid example where left part ≤ mid and right part ≥ mid
print(check(A, 0, len(A) - 1))  # Should print True

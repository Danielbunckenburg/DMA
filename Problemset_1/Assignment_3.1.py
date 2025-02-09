def find_triplet(a):
    n = len(a)
    found = False
    i = 0

    while i < n and not found:
        j = 0
        while j < n and not found:
            k = 0
            while k < n and not found:
                if i != j and j != k and i != k and a[i] + a[j] + a[k] == 0:
                    found = True
                    return (i, j, k)  # Return indices when a valid triplet is found
                k += 1
            j += 1
        i += 1

    if found:
        return (i, j, k)
    else:
        return "failed"

# Example usage:
a = [-1, 2, 1, 0, -2, 3]
result = find_triplet(a)
print(result)

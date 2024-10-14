# Time Complexity:   O(n)
# Memory Complexity: O(n)


from random import randint

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

def randomized_partition(A, p, r):
    i = p if p == r else randint(p, r)

    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x: #swap <= to > to search for i'th biggest
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i + 1]
    return i + 1

A = [1, 3, 2, 5]
k = 3
print(randomized_select(A,0,len(A)-1,k))

A = [897935, 1325657, 905326, 706311, 282251, 139169]
k = 1
print(randomized_select(A,0,len(A)-1,k))

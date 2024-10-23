# Time Complexity:   O(n)
# Memory Complexity: O(n)


from random import randint
import random
from sys import prefix

# ================================================================================
# Correct implementation
# def randomized_select(A, p, r, i):
#     if p == r:
#         return A[p]
#     q = randomized_partition(A, p, r)
#     k = q - p + 1
#     if i == k:
#         return A[q]
#     elif i < k:
#         return randomized_select(A, p, q - 1, i)
#     else:
#         return randomized_select(A, q + 1, r, i - k)

# def randomized_partition(A, p, r):
#     i = p if p == r else randint(p, r)

#     A[r], A[i] = A[i], A[r]
#     return partition(A, p, r)

# def partition(A, p, r):
#     x = A[r]
#     i = p - 1
#     for j in range(p, r):
#         if A[j] <= x: #swap <= to > to search for i'th biggest
#             i += 1
#             A[i], A[j] = A[j], A[i]
#     A[i+1], A[r] = A[r], A[i + 1]
#     return i + 1
# ================================================================================


# testing field
#
# [0,1,2,3,4]
# off 1
# step 2
#

def randomized_select_w_step_n_offset(A, i, step=1, offset=0, p=None, r=None):
    if p is None:
        p = offset
    if r is None:
        r = (len(A)-1-offset)//step*step+offset
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select_w_step_n_offset(A, i, step, offset, p, q - 1)
    else:
        return randomized_select_w_step_n_offset(A, i - k, step, offset, q + 1, r)

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

# def randomized_select_w_step_n_offset(A, i, step: int = 1, offset: int = 0, p = 0, r = None):
#     if step < 1:
#         raise ValueError(f"Step has to be positive integer, provided [{step}]")
#     if r is None:
#         r = len(A)//step*step-1
#         print("r", r, "A[r]", A[r])
#     else:
#         r = (r)//step*step
#         print("P", p, "R", r)
#     if offset < 0:
#         fix_by = offset//(r+1)
#         offset -= (r+1)*fix_by
#     def randomized_partition(A, p, r, step):
#         def partition(A, p, r, step):
#             x = A[r]
#             print("x", x)
#             i = p - step
#             for j in range(p, r, step):
#                 print(A)
#                 if A[j] <= x: #swap <= to > to search for i'th biggest
#                     print(A[j])
#                     i += step
#                     A[i], A[j] = A[j], A[i]
#             A[i+step], A[r] = A[r], A[i + step]
#             return i + step
#         # i = p if p == r else randint(p, r)
#         i = p if p == r else randint(0, (r-p)//step)*step + p
#         print("p", p, "r", r, "rand", i, flush=True)
#         A[r], A[i] = A[i], A[r]
#         return partition(A, p, r, step)
#     if p == r:
#         return A[p]
#     q = randomized_partition(A, p, r, step)
#     k = (q - p)//step + 1
#     if i == k:
#         return A[q]
#     elif i < k:
#         return randomized_select_w_step_n_offset(A, i, step, offset, p, q - step)
#     else:
#         return randomized_select_w_step_n_offset(A, i - k, step, offset, q + step, r)



# A = [1, 3, 2, 5]
# k = 3
# print(randomized_select(A,0,len(A)-1,k))

# A = [897935, 1325657, 905326, 706311, 282251, 139169]
# k = 1
# print(randomized_select(A,0,len(A)-1,k))

# arr = [1,4,3]
arr = [10,1,2,10,3,10]
k = 1
step = 3
print("res", randomized_select_w_step_n_offset(arr, k, step, 0))

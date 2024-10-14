# Time Complexity:   O(nlogn)
# Memory Complexity: O(n)
#
# Where n is len(s)
# I did not include other variables in the complexity as in some scenarios it might still all round up to n


from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def binary_search_geq(arr: List[int], target: int):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return left if left < len(arr) else -1

        def binary_search_leq(arr: List[int], target: int):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return right

        def binary_search_for_range(arr: List[int], target_min: int, target_max: int):
            # Time Complexity:   O(logn)
            # Memory Complexity: O(1)

            i_min = binary_search_geq(arr, target_min)
            i_max = binary_search_leq(arr, target_max)
            if i_min != -1 and i_max != -1 and i_min <= i_max:
                return i_min, i_max
            return None

        def KMPSearch(pat, txt):
            # Time Complexity:   O(n+m)
            # Memory Complexity: O(n+result)

            def computeLPSArray(pat):
                M = len(pat)
                lps = [0] * M
                length = 0
                i = 1
                while i < M:
                    if pat[i] == pat[length]:
                        length += 1
                        lps[i] = length
                        i += 1
                    else:
                        if length != 0:
                            length = lps[length - 1]
                        else:
                            lps[i] = 0
                            i += 1
                return lps

            M = len(pat)
            N = len(txt)
            lps = computeLPSArray(pat)
            result = []
            i = 0  # index for txt
            j = 0  # index for pat
            while (N - i) >= (M - j):
                if pat[j] == txt[i]:
                    j += 1
                    i += 1
                if j == M:
                    result.append(i - j)
                    j = lps[j - 1]
                elif i < N and pat[j] != txt[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return result

        a_occur = KMPSearch(a, s)
        b_occur = KMPSearch(b, s)

        result =[]
        for i in a_occur:
            if binary_search_for_range(b_occur, i-k, i+k):
                result.append(i)

        return result

# s = "isawsquirrelnearmysquirrelhouseohmy"
# a = "my"
# b = "squirrel"
# k = 15
# result = Solution().beautifulIndices(s, a, b, k)
# print(result, [16,33]) # [16,33]

# s = "abcd"
# a = "a"
# b = "a"
# k = 4
# result = Solution().beautifulIndices(s, a, b, k)
# print(result, [0]) # [0]

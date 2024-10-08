# Time Complexity:   O(n)
# Memory Complexity: O(1)


class Solution:
    def minSwaps(self, s: str) -> int:
        counter = maxi = 0
        for i in s:
            counter += -1 if i == "[" else 1
            maxi = max(maxi, counter)
        return (maxi + 1) // 2


# s = "][]["
# result = Solution().minSwaps(s)
# print(result) # 1

# s = "]]][[["
# result = Solution().minSwaps(s)
# print(result) # 2

# s = "]]]][[[["
# result = Solution().minSwaps(s)
# print(result) # 2

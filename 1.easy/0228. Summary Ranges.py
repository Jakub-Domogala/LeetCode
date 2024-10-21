# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        result = [[nums[0], nums[0]]]
        for i in range(1, n):
            if nums[i] - 1 == result[-1][1]:
                result[-1][1] = nums[i]
            else:
                result.append([nums[i], nums[i]])
        return ["->".join(str(x) for x in sorted(list(set(e)))) for e in result] # just formatting for output


# nums = [0,1,2,4,5,7]
# result = Solution().summaryRanges(nums)
# print(result)

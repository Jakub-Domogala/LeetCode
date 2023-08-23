# Time Complexity:   O(log(n))
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot():
            for i, e in enumerate(nums):
                if i >= 1 and e < nums[i-1]:
                    return i
            return 0
        def get_value(index):
            return nums[(index + pivot)%n]

        n, pivot = len(nums), get_pivot()
        back, front = 0, n-1
        position = front//2

        while back <= front:
            if get_value(position) == target:
                return (position + pivot)%n
            elif get_value(position) > target:
                front = position - 1
            else:
                back = position + 1
            position = (front - back)//2 + back
            
        return -1

# print(Solution().search([4,5,6,7,0,1,2], 0))
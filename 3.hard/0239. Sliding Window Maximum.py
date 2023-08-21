# Time Complexity:   O(n)
# Memory Complexity: O(n)

from collections import deque
from typing import List


class Solution(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        result = []

        def pop_smaller_than_new_elem_and_append_it():
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
            que.append(i)

        def pop_out_of_window():
            while que and que[0] <= i-k:
                que.popleft()

        def append_result():
            result.append(nums[que[0]])

        for i in range(k):
            pop_smaller_than_new_elem_and_append_it()

        for i in range(k, len(nums)):
            append_result()

            pop_out_of_window()
            pop_smaller_than_new_elem_and_append_it()

        append_result()

        return result


# expected [3,3,5,5,6,7]
# print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))

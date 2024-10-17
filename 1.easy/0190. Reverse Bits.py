# Time Complexity:   O(n)
# Memory Complexity: O(1) I wonder if 32bit int should count as O(n) here
#
# Added code for visualisation, uncomment it if you want to understand the solution better


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0
        # print(dev2bin(reversed))
        # print(dev2bin(n))
        # print()
        for i in range(32):
            reversed = (reversed << 1) + n%2
            n = n >> 1

            # print(dev2bin(reversed))
            # print(dev2bin(n))
            # print()
        return reversed

# def dev2bin(n):
#     s = ""
#     while n != 0:
#         s = str(n%2) + s
#         n = n >> 1
#     return s



# number = 43261596
# result = Solution().reverseBits(number)
# print(result, 964176192)

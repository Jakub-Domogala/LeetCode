# Time Complexity:   O(logn) if n wouldn't be constrainted
# Memory Complexity: O(1)


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bit_count = 0
        while left != right:
            left >>= 1
            right >>= 1
            bit_count += 1
        return left << bit_count

    # def rangeBitwiseAnd(self, left: int, right: int) -> int: # This is also O(logn) but not as nicely written, with bigger overhang computation, the approach was also quite a bit diffrent here
    #     bl = f"{left:032b}"
    #     br = f"{right:032b}"
    #     result = ""
    #     comp = 1 << 31
    #     for i in range(32):
    #         if bl[i] != br[i]:
    #             result += "0"
    #         elif comp < right - left:
    #             result += "0"
    #         elif right % (comp) >= left % (comp):
    #             result += bl[i]
    #         else:
    #             result += "0"
    #         comp = comp >> 1
    #     return int(result, 2)

# result = Solution().rangeBitwiseAnd(5, 7)
# print(result)

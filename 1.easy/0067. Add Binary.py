# Time Complexity:   O(max(n1, n2))
# Memory Complexity: O(max(n1, n2))


class Solution(object):
    def addBinary(self, bin1: str, bin2: str) -> str:
        bin1, bin2 = bin1[::-1], bin2[::-1]
        n1, n2 = len(bin1), len(bin2)
        result, rest = "", 0
        for i in range(max(n1, n2)):
            total = (
                (int(bin1[i]) if i < n1 else 0) + (int(bin2[i]) if i < n2 else 0) + rest
            )
            result = str(total % 2) + result
            rest = total // 2
        return "1" + result if rest else result


# print(Solution().addBinary('10', '11'))

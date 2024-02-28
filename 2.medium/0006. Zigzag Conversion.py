# Time Complexity:   O(n)
# Memory Complexity: O(n)


class Solution(object):
    def convert(self, s: str, numRows: int) -> str:
        def count_jump(num_rows: int, idx: int):
            idx = idx % ((num_rows - 1) * 2)
            res = (num_rows - idx - 1) * 2
            return res

        if numRows == 1:
            return s
        result = "".join([s[i] for i in range(0, len(s), 2 * numRows - 2)])
        line_index = 1
        while line_index < numRows - 1:
            index = line_index
            while index < len(s):
                result += s[index]
                if index + count_jump(numRows, index) >= len(s):
                    break
                result += s[index + count_jump(numRows, index)]
                index += (numRows - 1) * 2
            line_index += 1

        result += "".join([s[i] for i in range(numRows - 1, len(s), 2 * numRows - 2)])
        return result


# print(Solution().convert("PAYPALISHIRING", 4))

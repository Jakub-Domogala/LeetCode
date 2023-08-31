# Time Complexity:   O(n1*n2)
# Memory Complexity: O(n1+n2)
# Where n1, n2 are len(num1), len(num2)


class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        print(num1, num2)
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        num1 = [int(num1[i]) for i in range(n1)][::-1]
        num2 = [int(num2[i]) for i in range(n2)][::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += num1[i] * num2[j]
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        result = "".join([str(e) for e in result[::-1]]).lstrip("0")
        return result if result != "" else "0"


# print(Solution().multiply("123", "456"))

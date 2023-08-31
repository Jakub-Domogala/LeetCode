# Time Complexity:   O(1)
# Memory Complexity: O(1)


class Solution(object):
    def intToRoman(self, num):
        int2rom = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        result = ""
        for key in sorted(int2rom.keys(), reverse=True):
            amount = num // key
            result += int2rom[key] * amount
            num %= key
        return result


# print(Solution().intToRoman(927))

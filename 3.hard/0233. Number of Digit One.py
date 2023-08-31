class Solution(object):
    def countDigitOne(self, n: int) -> int:
        pass


def ones(n):  # bruteforce
    count = 0
    for i in range(n, -1, -1):
        s = str(i)
        for e in s:
            if e == "1":
                count += 1
    print(n, count, end="\t\n")

# Time Complexity:   O(n)
# Memory Complexity: O(n)


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        if n == 0:
            return True
        for i in range(1,n):
            if words[i-1][-1] != words[i][0]:
                return False
        return words[0][0] == words[-1][-1]

sentence = "leetcode exercises sound delightful"
print(Solution().isCircularSentence(sentence), True)
sentence = "leetcode exercises sound good"
print(Solution().isCircularSentence(sentence), False)
sentence = ""
print(Solution().isCircularSentence(sentence), True)
sentence = "oko"
print(Solution().isCircularSentence(sentence), True)

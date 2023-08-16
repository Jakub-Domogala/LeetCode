# Time Complexity:   O(n)
# Memory Complexity: O(c)

# it also contains protection for inputting wrong numbers
class Solution(object):
    def romanToInt(self, s: str) -> int:
      symbols = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
      combinations = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      result = 0
      previous_value = None
      repeated = 0
      i = 0
      while i < len(s):
          if i < len(s) - 1 and s[i:i+2] in combinations:
            result += combinations[s[i:i+2]]
            previous_value = symbols[s[i+1]]
            i += 2
          elif s[i] in symbols and (previous_value is None or previous_value >= symbols[s[i]]) and (repeated < 3 or previous_value != symbols[s[i]]):
            repeated = repeated + 1 if previous_value == symbols[s[i]] else 1
            result += symbols[s[i]]
            previous_value = symbols[s[i]]
            i += 1
          else:
             return False
      return result

# print(Solution().romanToInt("MDCCCLXXXIV"))
          
          

          
          

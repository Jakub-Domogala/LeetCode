# Time Complexity:   O(n)
# Memory Complexity: O(1)


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        if s.count('a') < k or s.count('b') < k or s.count('c') < k:
            return -1
        def get_id(c):
            return ord(c) - 97
        def is_solution(a):
            nonlocal k
            return (a[0] >= k
                and a[1] >= k
                and a[2] >= k)
        n = len(s)
        state = [0,0,0]
        f_idx = n
        b_idx = -1
        best_sol = n
        for i in range(n):
            state[get_id(s[i])] += 1
            if is_solution(state):
                bestsol = i+1
                f_idx = i
                break
        while f_idx >= -1 and b_idx < n:
            if is_solution(state):
                best_sol = min(best_sol, f_idx + b_idx + 2)
                state[get_id(s[f_idx])] -= 1
                f_idx -= 1
            else:
                b_idx += 1
                state[get_id(s[n-b_idx-1])] += 1
        return best_sol

# s = "cbbac"
# k = 1
# result = Solution().takeCharacters(s, k)
# print(result, 3)
# s = "aabaaaacaabc"
# k = 2
# result = Solution().takeCharacters(s, k)
# print(result, 8)

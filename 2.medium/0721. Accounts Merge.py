# I will not put complexity here cause this task is not fun for me

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts = sorted(accounts)
        merged = []

        def merge(merge_to_idxs, idx):
            merge_to_idxs = sorted(list(set(merge_to_idxs)))[::-1]
            all_emails = defaultdict(bool)
            pooped = []
            for i in merge_to_idxs:
                tmp_pooped = merged.pop(i)
                for j in range(1, len(tmp_pooped)):
                    all_emails[tmp_pooped[j]] = True
            for i in range(1, len(accounts[idx])):
                all_emails[accounts[idx][i]] = True
            merged.append([accounts[idx][0]])
            for key, value in all_emails.items():
                if value == True:
                    merged[-1].append(key)

        def check_merged(i):
            new_emails = defaultdict(bool)
            indexes = []
            for email in accounts[i][1:]:
                new_emails[email] = True
            for j, macc in enumerate(merged):
                if macc[0] != accounts[i][0]:
                    continue
                for email_idx in range(1, len(macc)):
                    if macc[email_idx] in new_emails:
                        indexes.append(j)
            return len(indexes) > 0, indexes

        n = len(accounts)
        for i in range(n):
            is_present, idx = check_merged(i)
            if is_present:
                merge(idx, i)
            else:
                merged.append(accounts[i])

        for i in range(len(merged)):
            merged[i] = [merged[i][0]] + sorted(list(set(merged[i][1:])))
        return merged


# accounts = [
#     ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
#     ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
#     ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
#     ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
#     ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"],
# ]
# print(Solution().accountsMerge(accounts))

// # Time Complexity:   O(n)
// # Memory Complexity: O(1)

#include <string>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, bool> charmap;
        int best = 1;
        int l = 0, r = 0;
        while (r < (int)s.length())
        {
            while (charmap.count(s[r]) && charmap[s[r]])
            {
                charmap[s[l]] = false;
                l++;
            }
            charmap[s[r]] = true;
            best = max(best, r - l + 1);
            r++;
        }
        return min(best, (int)s.length());
    }
};

// int main()
// {
//     Solution sol;
//     string s = "abcabcbb";
//     int result = sol.lengthOfLongestSubstring(s);
//     cout << result << endl;
//     s = "tmmzuxt";
//     result = sol.lengthOfLongestSubstring(s);
//     cout << result << endl;

//     return 0;
// }
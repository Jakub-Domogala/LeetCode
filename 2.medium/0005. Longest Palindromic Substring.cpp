// Time Complexity:   O(n^2)
// Memory Complexity: O(n)

// #include <string>
// #include <iostream>
// #include <vector>

// using namespace std;

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int rl = 0, rr = 0, rlen = 0;
        vector<int> expanded;
        for (int i = 0; i < (int)(s.size()); i++)
        {
            expanded = expandPalindrome(i, i, s);
            if (expanded[0] > rlen)
            {
                rlen = expanded[0], rl = expanded[1], rr = expanded[2];
            }
            if (i < (int)s.size() - 1)
            {
                expanded = expandPalindrome(i, i + 1, s);
                if (expanded[0] > rlen)
                {
                    rlen = expanded[0], rl = expanded[1], rr = expanded[2];
                }
            }
        }
        return s.substr(rl, rlen);
    }
    vector<int> expandPalindrome(int left, int right, string s)
    {
        while (left >= 0 && right < (int)s.length() && s[left] == s[right])
        {
            left--, right++;
        }
        return {right - left - 1, left + 1, right - 1};
    }
};

// int main()
// {
//     Solution sol;
//     string s = "a";
//     cout << "Longest palindrome: " << sol.longestPalindrome(s) << endl;
//     return 0;
// }
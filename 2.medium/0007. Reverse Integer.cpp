// #include <iostream>

// using namespace std;

class Solution
{
public:
    int reverse(int x)
    {
        int sign = 1;
        int64_t rest = x;
        if (x < 0)
        {
            sign = -1;
            rest = -rest
        }

        int64_t result = 0;
        while (rest > 0)
        {
            result *= 10;
            result += rest % 10;
            rest /= 10;
        }

        result = result * sign;

        return (result > INT32_MAX || result < INT32_MIN) ? 0 : result;
    }
};

// int main()
// {
//     Solution sol;
//     cout << "result/expected " << sol.reverse(123) << " / " << 321 << endl;
//     cout << "result/expected " << sol.reverse(-123) << " / " << -321 << endl;
//     cout << "result/expected " << sol.reverse(120) << " / " << 21 << endl;
// }
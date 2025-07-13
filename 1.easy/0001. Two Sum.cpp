#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        int n = nums.size();
        unordered_map<int, int> nums_map;
        for (int i = 0; i < n; i++)
        {
            nums_map[nums[i]] = i;
        }
        for (int i = 0; i < n; i++)
        {
            int complement = target - nums[i];
            if (nums_map.count(complement) && nums_map[complement] != i)
            {
                return {i, nums_map[complement]};
            }
        }
        return {};
    }
};

int main()
{
    Solution solution;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> expected = {0, 1};
    vector<int> result = solution.twoSum(nums, target);
    cout << "Result: " << result[0] << ", " << result[1] << endl;
    cout << "Expected: " << expected[0] << ", " << expected[1] << endl;
    return 0;
}
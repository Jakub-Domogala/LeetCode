class Solution {

    public int[] twoSum(int[] nums, int target) {
        int[][] withIdx = addIndexesToArr(nums);
        Arrays.sort(withIdx, (a, b) -> Integer.compare(a[0], b[0]));
        int front = 0, back = nums.length - 1;
        while (front < back) {
            if (withIdx[front][0] + withIdx[back][0] == target) {
                return new int[] { withIdx[front][1], withIdx[back][1] };
            } else if (withIdx[front][0] + withIdx[back][0] <= target) {
                front++;
            } else back--;
        }
        return new int[] { -1 };
    }

    public int[][] addIndexesToArr(int[] nums) {
        int[][] result = new int[nums.length][2];
        for (int i = 0; i < nums.length; i++) {
            result[i][0] = nums[i];
            result[i][1] = i;
        }
        return result;
    }
}

class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        int[] rightSum = new int[n];

        int sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            rightSum[i] = sum;
            sum += nums[i];
        }

        sum = 0;
        for (int i = 0; i < n; i++) {
            if (sum == rightSum[i]) {
                return i;
            }
            sum += nums[i];
        }

        return -1;
    }

    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.pivotIndex(new int[] {1, 7, 3, 6, 5, 6}));
        System.out.println(s.pivotIndex(new int[] {1, 2, 3}));
        System.out.println(s.pivotIndex(new int[] {2, 1, -1}));
    }
}

class Solution {
    public int findMiddleIndex(int[] nums) {
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
        System.out.println(s.findMiddleIndex(new int[] {2, 3, -1, 8, 4}));
        System.out.println(s.findMiddleIndex(new int[] {1, -1, 4}));
        System.out.println(s.findMiddleIndex(new int[] {2, 5}));
    }
}

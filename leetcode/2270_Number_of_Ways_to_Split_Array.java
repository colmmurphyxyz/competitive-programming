class Solution {
    public int waysToSplitArray(int[] nums) {
        int n = nums.length;
        long[] sums = new long[n];
        long[] revSums = new long[n];
        
        long sum = 0L;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            sums[i] = sum;
        }
        sum = 0;
        for (int i = n - 1; i > 0; i--) {
            sum += nums[i];
            revSums[i] = sum;
        }

        int numSplits = 0;
        for (int i = 0; i < n - 1; i++) {
            if (sums[i] >= revSums[i + 1]) {
                numSplits++;
            }
        }
        return numSplits;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.waysToSplit(new int[] {10, 4, -8, 7}));
        System.out.println(s.waysToSplit(new int[] {2, 3, 1, 0}));
    }
}
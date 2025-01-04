class Solution {
    public int waysToSplitArray(int[] nums) {
        int n = nums.length;
        long[] sums = new long[n];
        
        long sum = 0L;
        for (int i = 0; i < n; i++) { // n iterations
            sum += nums[i];
            sums[i] = sum;
        }

        long threshold = (long) Math.ceil(sum / 2.0);

        int numSplits = 0;
        for (int i = 0; i < n - 1; i++) {
            if (sums[i] >= threshold) {
                numSplits++;
            }
        }
        return numSplits;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.waysToSplitArray(new int[] {10, 4, -8, 7}));
        System.out.println(s.waysToSplitArray(new int[] {2, 3, 1, 0}));
    }
}
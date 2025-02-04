import java.lang.Math;

class Solution {
    public int maxAscendingSum(int[] nums) {
        int sum = nums[0];
        int maximum = sum;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] < nums[i]) {
                sum += nums[i];
            } else {
                sum = nums[i];
            }
            maximum = Math.max(sum, maximum);
        }
        return maximum;
    }

    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.maxAscendingSum(new int[] {10,20,30,5,10,50}));
        System.out.println(s.maxAscendingSum(new int[] {10,20,30,40,50}));
        System.out.println(s.maxAscendingSum(new int[] {12,17,15,13,10,11,12}));
    }
}
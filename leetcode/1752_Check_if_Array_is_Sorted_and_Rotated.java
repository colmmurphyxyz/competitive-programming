import java.util.Arrays;

class Solution {
    // public boolean check(int[] nums) {
    //     if (nums.length <= 1) return true;
    //     int[] diffs = new int[nums.length];
    //     int curr = 0;
    //     for (int i = 0; i < nums.length; i++) {
    //         diffs[i] = nums[i] - curr;
    //         curr = nums[i];
    //     }
    //     diffs[0] = nums[0] - nums[nums.length - 1];
    //     System.out.println(Arrays.toString(diffs));
    //     return Arrays.stream(diffs).filter(it -> it < 0).count() <= 1;
    // }

    public boolean check(int[] nums) {
        if (nums.length <= 1) return true;
        int negativeCount = 0;
        for (int i = 1; i < nums.length; i++) {
            int diff = nums[i] - nums[i - 1];
            if (diff < 0) negativeCount++;
        }
        if (nums[0] - nums[nums.length - 1] < 0) negativeCount++; 
        return negativeCount <= 1;
    }
 
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.check(new int[] {3, 4, 5, 1, 2}));
        System.out.println(s.check(new int[] {2, 1, 3, 4}));
        System.out.println(s.check(new int[] {1, 2, 3}));
    }
}
import java.util.Arrays;
import java.lang.Math;;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double currentSum = Arrays.stream(Arrays.copyOfRange(nums, 0, k)).sum();
        double currentMax = currentSum;
        for (int i = 1; i <= nums.length - k; i++) {
            currentSum -= nums[i - 1];
            currentSum += nums[i + k - 1];
            currentMax = Math.max(currentMax, currentSum);
        }

        return currentMax / (double) k;
    }
}
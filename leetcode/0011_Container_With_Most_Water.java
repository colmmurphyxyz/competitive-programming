import java.lang.Math;

class Solution {
    private int getArea(int[] height, int left, int right) {
        return Math.min(height[left], height[right]) * (right - left);
    }
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            maxArea = Math.max(maxArea, getArea(height, left, right));

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maxArea(new int[] {1, 8, 6, 2, 5, 4, 8, 3, 7}));
        System.out.println(s.maxArea(new int[] {1, 1}));
        System.out.println(s.maxArea(new int[] {2,3,4,5,18,17,6}));
    }
}

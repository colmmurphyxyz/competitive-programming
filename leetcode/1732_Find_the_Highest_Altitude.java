import java.lang.Math;

class Solution {
    public int largestAltitude(int[] gain) {
        int sum = 0;
        int max = 0;
        for (int i = 0; i < gain.length; i++) {
            sum += gain[i];
            max = Math.max(max, sum);
        }
        return max;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.largestAltitude(new int[] {-5, 1, 5, 0, -7}));
        System.out.println(s.largestAltitude(new int[] {-4, -3, -2, -1, 4, 3, 2}));
    }
    
}

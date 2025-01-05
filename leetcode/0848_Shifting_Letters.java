class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        long[] sums = new long[shifts.length];
        long sum = 0L;
        for (int i = s.length() - 1; i >= 0; i--) {
            sum += shifts[i];
            sums[i] = sum;
        }
        for (long d: sums) {
            System.out.printf("%d, ", d);
        }
        System.out.println();
        char[] ans = new char[s.length()];
        for (int i = 0; i < s.length(); i++) {
            ans[i] = shift(s.charAt(i), sums[i]);
        }
        return new String(ans);
    }

    private char shift(char c, long delta) {
        return (char) (Math.floorMod(((int) c - 97) + delta, 26) + 97);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.shiftingLetters("abc", new int[] {3, 5, 9}));
        System.out.println(s.shiftingLetters("aaa", new int[] {1, 2, 3}));
    }
}